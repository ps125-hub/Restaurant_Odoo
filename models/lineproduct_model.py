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
    state = fields.Selection(string="Status",selection=[('P','Prepare'),('D','Done'),],default="P")
    
    @api.depends('product_id.price','quantity')
    def _calcPrice(self):
        for rec in self:
            self.price = rec.product_id.price*rec.quantity
    @api.depends('orders.state')
    def confirmInvoice(self):
        self.ensure_one()
        if self.state == "P":
            self.state = "D"
        