from odoo import models, fields, api
from datetime import datetime
class InvoiceModel(models.Model):
    _name = 'restaurant_app.invoice_model'
    _description='This is the invoice model'
    ref = fields.Integer(string ='Ref',help ='Id of invoice',required =True, index = True)
    date = fields.Datetime(string ='Date',help ='Date of invoice',required =True, default = lambda self:datetime.now())
    base = fields.Float(string ='Base', help = 'Base price of a invoice',required =True, default =0)
    vat = fields.Selection(string ='VAT', help = 'VAT of a invoice',selection =[],required = True)
    total = fields.Float(string='Total', help = 'Total of a invoice',compute ='_totalPrice',required =True, default =0)
    lineProducts = fields.One2many("restaurant_app.lineproduct_model",'invoice_id',string ='Lines',help = 'Line of the product')
    @api.depends('lineProduct.quantity','lineProduct.price')
    def _totalPrice(self):
        for lineProduct in self.lineProducts:
            self.base += lineProduct.price