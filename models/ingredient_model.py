from odoo import models,fields,api
class IngredientModel(models.Model):
    _name='restaurant_app.ingredient_model'
    _description='This is the ingredient model'

    name = fields.Char(string ="Ingredient",help="Name of the ingredient",required=True,index=True)
    allergen = fields.Char(string ="Allergen",help="Allergen of the ingredient",required=False)
    comentari = fields.Text(string="Comentari",help="Comentari of the ingredient")
    products = fields.Many2many("restaurant_app.product_model",relation="product2ingredient",string="Products")