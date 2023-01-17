from odoo import models, fields, api
from datetime import date,datetime
class InvoiceModel(models.Model):
    _name = 'restaurant_app.invoice_model'
    _description='This is the invoice model'
    _rec_name = 'ref'
    _sql_constraints = [('restaurant_ref_uniq','UNIQUE (ref)','There cannot be two invoice with the same ref!!'),]

    ref = fields.Integer(string ='Ref',help ='Id of invoice',required =True,readonly=1, index = True,default =lambda self:self.refAutoincrement())
    client = fields.Char (string='Client',help='Name of the client')
    date = fields.Date(string ='Date',help ='Date of invoice',required =True, default = lambda self:date.today())
    currency_id = fields.Many2one('res.currency',string="Currency",default=lambda self:self.env.user.company_id.currency_id)
    base = fields.Monetary(string ='Base', help = 'Base price of a invoice',compute ='_priceBase',store=True,required =True,readonly=1, default =0)
    vat = fields.Selection(string ='VAT', help = 'VAT of a invoice',selection =[('0','0%'),('4','4%'),('10','10%'),('21','21%')],required = True,default='10')
    total = fields.Monetary(string='Total', help = 'Total of a invoice',compute ='_totalPrice',store=True,required =True, default =0,readonly=1)
    lineProducts = fields.One2many("restaurant_app.lineproduct_model",'invoice_id',string ='Lines',compute = "_addLineProduct",store=True,help = 'Line of the product')
    orders = fields.One2many("restaurant_app.order_model","invoice_id",string="Orders", help="List order")
    state = fields.Selection(string="Status",selection=[('D','Draft'),('C','Confirmed'),],default="D")

    @api.depends('lineProducts.quantity','lineProducts.price')
    def _priceBase(self):
        self.base = 0
        for lineProduct in self.lineProducts:
            self.base += lineProduct.price

    @api.depends('base','vat')
    def _totalPrice(self):
        if self.vat =='0':
            self.total=self.base
        elif self.vat =='4':
            self.total = self.base+(self.base*0.04)
        elif self.vat == '10':
            self.total = self.base+(self.base*0.1)
        elif self.vat == '21':
            self.total = self.base+(self.base*0.21)

    @api.depends('orders.state')
    def confirmInvoice(self):
        self.ensure_one()
        if self.state == "D":
            self.state = "C"

    def refAutoincrement(self):
        id = self.env['restaurant_app.invoice_model'].search_read()
        if len(id) == 0:
            return 1
        return id[-1]["ref"]+1
