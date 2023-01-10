from odoo import models, fields, api

class CategoryModel(models.Model):
    _name = 'restaurant_app.category_model'
    _description='This is the category model'
    _rec_name = 'complete_name'
    _order = 'complete_name'

    name=fields.Char(string="Category",help="Name of the category",required=True,index=True)
    complete_name = fields.Char('Complete Name', compute='_compute_complete_name',recursive = True,store = True)
    description = fields.Text(string="Description",help="Description of the category",required=True)
    products=fields.One2many("restaurant_app.product_model","category_id",string="Products")
    totalProduts = fields.Integer("Total Products",compute="_total",store=True)
    parent_id = fields.Many2one("restaurant_app.category_model",string = "Parent Category",index=True, ondelete ='cascade')
    child_ids = fields.One2many("restaurant_app.category_model","parent_id",string = "Childs category")
    @api.depends("products.category_id")
    def _total(self):
        self.totalProduts= len(self.products)
    @api.depends('name','parent_id.complete_name')
    def _compute_complete_name(self):
        for category in self:
            if category.parent_id:
                category.complete_name = '%s / %s' % (category.parent_id.complete_name, category.name)
            else:
                category.complete_name = category.name
