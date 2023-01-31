from odoo import api,models,fields

class ProductModel(models.Model):
    _name='restaurant_app.product_model'
    _description = 'This is the product model'
    
    name = fields.Char(string = "Product name",help="Name of the product",required=True,index=True)
    description = fields.Text(string="Description",help="Description of the product")
    currency_id = fields.Many2one('res.currency',string="Currency",default=lambda self:self.env.user.company_id.currency_id)
    price = fields.Monetary(string="Price", help="Price of the product",required=False)
    categories = fields.Many2many("restaurant_app.category_model",relation='category2product',string="Categories")
    ingredients=fields.Many2many("restaurant_app.ingredient_model",relation="product2ingredient",string="Ingredients")
    image = fields.Binary(help="image of the student")
    lineProducts = fields.One2many("restaurant_app.lineproduct_model","product_id",string="Line products")
    totalIng = fields.Integer("Total Ingredients",compute="_total",store=True)
    @api.depends("ingredients")
    def _total(self):
        self.totalIng= len(self.ingredients)

