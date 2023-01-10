from odoo import models, fields, api
class LineProductModel(models.Model):
    _name='restaurant_app.lineproduct_model'
    _description='This is the line product model'
    
    invoice_id = fields.Many2one('restaurant_app.invoice_model', string ='Invoice')
    order_id = fields.Many2one('restaurant_app.order_model',string="Order")
    product_id = fields.Many2one('restaurant_app.product_model',string="Product")
    quantity = fields.Integer(string="Quantity",help="Quantity of the product",required=True)
    price  = fields.Float(string="Price",help="Price of the line product",default="0")
