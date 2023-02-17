from odoo import models, fields, api
class LineProductModel(models.Model):
    _name='restaurant_app.lineproduct_model'
    _description='This is the line product model'
    
    invoice_id = fields.Many2one('restaurant_app.invoice_model', string ='Invoice',ondelete = "cascade")
    order_id = fields.Many2one('restaurant_app.order_model',string="Order",ondelete = "cascade")
    product_id = fields.Many2one('restaurant_app.product_model',string="Product",ondelete = "cascade")
    quantity = fields.Integer(string="Quantity",help="Quantity of the product",required=True, default=1)
    currency_id = fields.Many2one('res.currency',string="Currency",default=lambda self:self.env.user.company_id.currency_id)
    price  = fields.Monetary(string="Price",help="Price of the line product",compute = '_calcPrice',readonly=1,store = True)
    state = fields.Selection(string="Status",selection=[('P','Prepare'),('D','Done'),("C","Collected")],default="P")
    @api.depends('product_id.price','quantity')
    def _calcPrice(self):
        for rec in self:
            self.price = rec.product_id.price*rec.quantity

    def buttonLineOrderAdmin(self):
        self.ensure_one()
        if self.state == "P":
            self.state = "D"
        elif self.state =="D":
            self.state = "C"
        #return {
        #    'name': ('OrderLine Admin List'),
        #    'view_type': 'form',
        #    'view_mode': 'tree,form',
        #    'res_model': 'restaurant_app.lineproduct_model',
        #    'view_id': False,
        #    'views':[
        #        (self.env.ref('restaurant_app.lineProduct_list_tree_admin').id,'tree'),
        #        (self.env.ref('restaurant_app.lineProduct_admin_form').id,'form')
        #        ],
        #    'type': 'ir.actions.act_window',
        #    'target': 'current',
        #    'nodestroy': True
        #}
    def buttonLineOrderWaiter(self):
        self.ensure_one()
        if self.state == "D":
            self.state = "C"

        #return {
        #    'name': ('OrderLine Waiter List'),
        #    'view_type': 'form',
        #    'view_mode': 'tree,form',
        #    'res_model': 'restaurant_app.lineproduct_model',
        #    'view_id': False,
        #    'views':[
        #        (self.env.ref('restaurant_app.lineProduct_list_tree_waiter').id,'tree'),
        #        (self.env.ref('restaurant_app.lineProduct_model_form_waiter').id,'form')
        #        ],
        #    'type': 'ir.actions.act_window',
        #    'target': 'current',
        #    'nodestroy': True
       # }
    def buttonLineOrderCooker(self):
        self.ensure_one()
        if self.state == "P":
            self.state = "D"
        #return {
        #    'name': ('OrderLine Cooker List'),
        #    'view_type': 'form',
        #    'view_mode': 'tree,form',
        #    'res_model': 'restaurant_app.lineproduct_model',
        #    'view_id': False,
        #    'views':[
        #        (self.env.ref('restaurant_app.lineProduct_list_tree_cooker').id,'tree'),
        #        (self.env.ref('restaurant_app.lineProduct_model_form_cooker').id,'form')
        #        ],
        #    'type': 'ir.actions.act_window',
        #    'target': 'current',
        #    'nodestroy': True
        #}
    def buttonLineOrderBarman(self):
        self.ensure_one()
        if self.state == "P":
            self.state = "D"
        #return {
        #    'name': ('OrderLine Barman List'),
        #    'view_type': 'form',
        #    'view_mode': 'tree,form',
        #    'res_model': 'restaurant_app.lineproduct_model',
        #    'view_id': False,
        #    'views':[
        #        (self.env.ref('restaurant_app.lineProduct_list_tree_barman').id,'tree'),
        #        (self.env.ref('restaurant_app.lineProduct_model_form_barman').id,'form')
        #        ],
        #    'type': 'ir.actions.act_window',
        #    'target': 'current',
        #    'nodestroy': True
        #}

    def buttonLineOrderTree(self):
        self.ensure_one()
        if self.state == "P":
            self.state = "D"
        elif self.state =="D":
            self.state = "C"
