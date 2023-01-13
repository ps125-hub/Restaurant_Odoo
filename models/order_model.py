from odoo import models,fields,api
from odoo.exceptions import ValidationError

class IngredientModel(models.Model):
    _name='restaurant_app.order_model'
    _description='This is the order model'
    _rec_name ='table'

    table = fields.Integer(string="Table",required=True)
    client = fields.Char(string ="Client",help="Name of the client",required = True, compute = "_createClient",store=True,recursive=True)
    pax = fields.Integer(string="Pax",help="Number of the person",required=True,default=1)
    waiter = fields.Char(string="Waiter",help="Name of the waiter",required=True, default = lambda self:self.env.user.name)
    product_id = fields.Many2one("restaurant_app.product_model",string="Product")
    currency_id = fields.Many2one('res.currency',string="Currency",default=lambda self:self.env.user.company_id.currency_id)
    priceTotal = fields.Monetary(string="Price total",help="Total price of the table",compute="_totalPrice",store=True,readonly=1)
    lineProducts = fields.One2many("restaurant_app.lineproduct_model","order_id",string="Line products")
    invoice_id = fields.Many2one("restaurant_app.invoice_model",string = "Invoice", compute="_createInvoice",store=True,recursive=True)
    state = fields.Selection(string="Status",selection=[('D','Draft'),('C','Confirmed'),],default="D")
    active = fields.Boolean(string = "Is the order active?",help="The task is order??",default=True)
    
    @api.depends('table')
    def _createClient(self):
        self.client = "table_"+str(self.table)

    @api.depends("lineProducts.quantity","lineProducts.product_id.price")
    def _totalPrice(self):
        self.priceTotal=0
        for rec in self.lineProducts:
            self.priceTotal+=(rec.quantity*rec.product_id.price)

    def confirmInvoice(self):
        self.ensure_one()
        if self.state == "D":
            self.state = "C"
            self.active=False

    @api.depends("state")  
    def _createInvoice(self):
        if(self.state =='C'):
            invoice = self.env["restaurant_app.invoice_model"].sudo().create({"client": self.client,"lineProducts": self.lineProducts})
            self.invoice_id = invoice