from odoo import models,fields,api
from odoo.exceptions import ValidationError

class OrderModel(models.Model):
    _name='restaurant_app.order_model'
    _description='This is the order model'
    _rec_name ='table'

    table = fields.Integer(string="Table",required=True,index = True)
    client = fields.Char(string ="Client",help="Name of the client",required = True, compute = "_createClient",store=True)
    pax = fields.Integer(string="Pax",help="Number of the person",required=True,default=1)
    waiter = fields.Char(string="Waiter",help="Name of the waiter",required=True, default = lambda self:self.env.user.name)
    product_id = fields.Many2one("restaurant_app.product_model",string="Product")
    currency_id = fields.Many2one('res.currency',string="Currency",default=lambda self:self.env.user.company_id.currency_id)
    priceTotal = fields.Monetary(string="Price total",help="Total price of the table",compute="_totalPrice",store=True,readonly=1)
    lineProducts = fields.One2many("restaurant_app.lineproduct_model","order_id",string="Line products")
    invoice_id = fields.Many2one("restaurant_app.invoice_model",string = "Invoice", compute="_createInvoice",store=True)
    state = fields.Selection(string="Status",selection=[('D','Draft'),('C','Confirmed'),],default="D")
    active = fields.Boolean(string = "Is the order active?",help="The active is order??",default=True)
    isdone = fields.Boolean(string="Is done?",help="The order is done?",compute="_isDone",store=True)
    isdoneline = fields.Boolean(string="Is done line?",help="The orderline is done?",compute="_isDoneLine",store=True,default =False)

    @api.onchange("isdone")
    def _changeActiveTask(self):
        self.active = not self.isdone
        self.isdone = not self.active

    @api.depends("lineProducts.state")
    def _isDoneLine(self):
        result = False
        for rec in self.lineProducts:
            if rec.state == "D":
                result = True
                break
        self.isdoneline = result
        
    @api.depends("lineProducts.state")
    def _isDone(self):
        result = True
        for rec in self.lineProducts:
            if rec.state !="C":
                result=False
        self.isdone = result
    
    @api.constrains("table")
    def _numTable(self):
        num=0
        records = self.env["restaurant_app.order_model"].search([])
        for rec in records:
            if rec.table == self.table:
                num+=1
                if num ==2:
                    raise ValidationError("There cannot be two order with the same table!!")
    @api.onchange('table')
    def _createClient(self):
        for rec in self:
            self.client = "table_"+str(rec.table)

    @api.depends("lineProducts.quantity","lineProducts.price")
    def _totalPrice(self):
        self.priceTotal=0
        for rec in self.lineProducts:
            self.priceTotal+=rec.price

    def confirmInvoice(self):
        self.ensure_one()
        if self.state == "D":
            self.state = "C"
            self.active=False
            if self.isdone ==False:
                    raise ValidationError("You cannot confirm that there is still a pending order line!!")
            return {
            'name': ('Order App'),
            'view_type': 'form',
            'view_mode': 'kanban,tree,form',
            'res_model': 'restaurant_app.order_model',
            'view_id': False,
            #'views':[
            #(self.env.ref('restaurant_app.action_window_order_model_kanban').id,'kanban'),
            #(self.env.ref('restaurant_app.order_list_tree').id,'tree'),
            #(self.env.ref('restaurant_app.order_model_form').id,'from')],
            'type': 'ir.actions.act_window',
            'target': 'current',
            'nodestroy': True
            }

    @api.depends("state")  
    def _createInvoice(self):
        if(self.state =='C'):
            invoice = self.env["restaurant_app.invoice_model"].sudo().create({"client": self.client,"lineProducts": self.lineProducts})
            self.invoice_id = invoice

    
