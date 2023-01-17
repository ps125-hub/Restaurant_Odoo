import mimetypes
from odoo import http
from odoo.http import json
from odoo import models, fields, api
from odoo.http import json,request,Response

class RestaurantApp(http.Controller):
    @http.route(['/restaurant_app/getIngredient','/restaurant_app/getIngredient/<int:idingred>'],auth='public', type='http')
    def getIngredient(self,idingred=None, **kw):
        if idingred:
            domain=[("id","=",idingred)]
        else:
            domain=[]
        ingredientdata = http.request.env["restaurant_app.ingredient_model"].sudo().search_read(domain,["name","allergen","comentari","products"])
        data={  
            #"status":200,
            "data":ingredientdata 
            }
        return http.Response(json.dumps(data).encode("utf8"),mimetype="application/json")

    @http.route(['/restaurant_app/getProduct','/restaurant_app/getProduct/<int:idproduct>'],auth='public', type='http')
    def getProduct(self,idproduct=None, **kw):
        if idproduct:
            domain=[("id","=",idproduct)]
        else:
            domain=[]
        productdata = http.request.env["restaurant_app.product_model"].sudo().search_read(domain,["name","description","currency_id","price","categories","ingredients"])
        data={  
            #"status":200,
            "data":productdata 
            }
        return http.Response(json.dumps(data).encode("utf8"),mimetype="application/json")
    @http.route(['/restaurant_app/getCategory','/restaurant_app/getCategory/<int:idcategory>'],auth='public', type='http')
    def getCategory(self,idcategory=None, **kw):
        if idcategory:
            domain=[("id","=",idcategory)]
        else:
            domain=[]
        categoriadata = http.request.env["restaurant_app.category_model"].sudo().search_read(domain,["name","description","products"])
        data={  
            #"status":200,
            "data":categoriadata 
            }
        return http.Response(json.dumps(data).encode("utf8"),mimetype="application/json")
    @http.route(['/restaurant_app/getInvoice','/restaurant_app/getInvoice/<int:idinvoice>'],auth='public', type='http')
    def getCategory(self,idinvoice=None, **kw):
        if idinvoice:
            domain=[("id","=",idinvoice)]
        else:
            domain=[]
        invoicedata = http.request.env["restaurant_app.invoice_model"].sudo().search_read(domain,["ref","client","base","vat","total","lineProducts","orders","state"])
        data={  
            #"status":200,
            "data":invoicedata 
            }
        return http.Response(json.dumps(data).encode("utf8"),mimetype="application/json")

    @http.route('/restaurant_app/addIngredient',auth='public', type='json',method="POST")
    def addIngredient(self, **kw):
        response = request.jsonrequest
        try:
            ingredientdata = http.request.env["restaurant_app.ingredient_model"].sudo().create(response)
            data={  
                "status":201,
                "data":ingredientdata.id
                }
            return data
        except Exception as e:
            data={  
                "status":404,
                "error":e 
                }
            return data

    @http.route('/restaurant_app/addProduct',auth='public', type='json',method="POST")
    def addProduct(self, **kw):
        response = request.jsonrequest
        try:
            productdata = http.request.env["restaurant_app.product_model"].sudo().create(response)
            data={  
                "status":201,
                "data":productdata.id
                }
            return data
        except Exception as e:
            data={  
                "status":404,
                "error":e 
                }
            return data

    @http.route('/restaurant_app/addCategory',auth='public', type='json',method="POST")
    def addCategory(self, **kw):
        response = request.jsonrequest
        try:
            productdata = http.request.env["restaurant_app.category_model"].sudo().create(response)
            data={  
                "status":201,
                "data":productdata.id
                }
            return data
        except Exception as e:
            data={  
                "status":404,
                "error":e 
                }
            return data

    @http.route('/restaurant_app/updateIngredient',auth='public', type='json',method="PUT")
    def updateIngredient(self, **kw):
        response = request.jsonrequest
        try:
            ingredientdata = http.request.env["restaurant_app.ingredient_model"].sudo().search([("id","=",response["id"])])
            ingredientdata.sudo().write(response)
            data={  
                "status":200,
                }
            return data
        except Exception as e:
            data={  
                "status":404,
                "error":e 
                }
            return data
    @http.route('/restaurant_app/updateProduct',auth='public', type='json',method="PUT")
    def updateProduct(self, **kw):
        response = request.jsonrequest
        try:
            productdata = http.request.env["restaurant_app.product_model"].sudo().search([("id","=",response["id"])])
            productdata.sudo().write(response)
            data={  
                "status":200,
                }
            return data
        except Exception as e:
            data={  
                "status":404,
                "error":e 
                }
            return data
    @http.route('/restaurant_app/updateCategory',auth='public', type='json',method="PUT")
    def updateCategory(self, **kw):
        response = request.jsonrequest
        try:
            categorydata = http.request.env["restaurant_app.category_model"].sudo().search([("id","=",response["id"])])
            categorydata.sudo().write(response)
            data={  
                "status":200,
                }
            return data
        except Exception as e:
            data={  
                "status":404,
                "error":e 
                }
            return data

    @http.route('/restaurant_app/delIngredient',auth='public', type='json',method="DELETE")
    def delIngredient(self, **kw):
        response = request.jsonrequest
        try:
            ingredientdata = http.request.env["restaurant_app.ingredient_model"].sudo().search([("id","=",response["id"])])
            ingredientdata.sudo().unlink()
            data={  
                "status":200,
                }
            return data
        except Exception as e:
            data={  
                "status":404,
                "error":e 
                }
            return data

    @http.route('/restaurant_app/delProduct',auth='public', type='json',method="DELETE")
    def delProduct(self, **kw):
        response = request.jsonrequest
        try:
            productdata = http.request.env["restaurant_app.product_model"].sudo().search([("id","=",response["id"])])
            productdata.sudo().unlink()
            data={  
                "status":200,
                }
            return data
        except Exception as e:
            data={  
                "status":404,
                "error":e 
                }
            return data

    @http.route('/restaurant_app/delCategory',auth='public', type='json',method="DELETE")
    def delCategory(self, **kw):
        response = request.jsonrequest
        try:
            categorydata = http.request.env["restaurant_app.category_model"].sudo().search([("id","=",response["id"])])
            categorydata.sudo().unlink()
            data={  
                "status":200,
                }
            return data
        except Exception as e:
            data={  
                "status":404,
                "error":e 
                }
            return data

    @http.route(['/restaurant_app/getOrder','/restaurant_app/getOrder/<int:idorder>'],auth='public', type='http')
    def getOrder(self,idorder=None, **kw):
        if idorder:
            domain=[("id","=",idorder)]
        else:
            domain=[]
        orderdata = http.request.env["restaurant_app.order_model"].sudo().search_read(domain,["table","client","pax","waiter","product_id","priceTotal","lineProducts","state","active"])
        data={  "status":200,
            "data":orderdata 
            }
        return http.Response(json.dumps(data).encode("utf8"),mimetype="application/json")
    @http.route('/restaurant_app/addOrder',auth='public', type='json',method="POST")
    def addOrder(self, **kw):
        response = request.jsonrequest
        try:
            orderdata = http.request.env["restaurant_app.order_model"].sudo().create(response)
            data={  
                "status":201,
                "data":orderdata.id
                }
            return data
        except Exception as e:
            data={  
                "status":404,
                "error":e 
                }
            return data
    @http.route('/restaurant_app/updateOrder',auth='public', type='json',method="PUT")
    def updateOrder(self, **kw):
        response = request.jsonrequest
        try:
            orderdata = http.request.env["restaurant_app.order_model"].sudo().search([("id","=",response["id"])])
            orderdata.sudo().write(response)
            data={  
                "status":200,
                "data":orderdata.id,
                }
            return data
        except Exception as e:
            data={  
                "status":404,
                "error":e 
                }
            return data
    @http.route('/restaurant_app/delOrder',auth='public', type='json',method="DELETE")
    def delOrder(self, **kw):
        response = request.jsonrequest
        try:
            orderdata = http.request.env["restaurant_app.order_model"].sudo().search([("id","=",response["id"])])
            orderdata.sudo().unlink()
            data={  
                "status":200,
                }
            return data
        except Exception as e:
            data={  
                "status":404,
                "error":e 
                }
            return data
    @http.route(['/restaurant_app/getLineproduct','/restaurant_app/getLineproduct/<int:idline>'],auth='public', type='http')
    def getLineproduct(self,idline=None, **kw):
        if idline:
            domain=[("id","=",idline)]
        else:
            domain=[]
        linedata = http.request.env["restaurant_app.lineproduct_model"].sudo().search_read(domain,["order_id","product_id","quantity","price"])
        data={  "status":200,
            "data":linedata 
            }
        return http.Response(json.dumps(data).encode("utf8"),mimetype="application/json")
    @http.route('/restaurant_app/addLineproduct',auth='public', type='json',method="POST")
    def addLineproduct(self, **kw):
        response = request.jsonrequest
        try:
            linedata = http.request.env["restaurant_app.lineproduct_model"].sudo().create(response)
            data={  
                "status":201,
                "data":linedata.id
                }
            return data
        except Exception as e:
            data={  
                "status":404,
                "error":e 
                }
            return data
    @http.route('/restaurant_app/updateLineperoduct',auth='public', type='json',method="PUT")
    def updateLineperoduct(self, **kw):
        response = request.jsonrequest
        try:
            orderdata = http.request.env["restaurant_app.lineproduct_model"].sudo().search([("id","=",response["id"])])
            orderdata.sudo().write(response)
            data={  
                "status":200,
                "data":orderdata.id,
                }
            return data
        except Exception as e:
            data={  
                "status":404,
                "error":e 
                }
            return data
    @http.route('/restaurant_app/delLineproduct',auth='public', type='json',method="DELETE")
    def delLineproduct(self, **kw):
        response = request.jsonrequest
        try:
            orderdata = http.request.env["restaurant_app.lineproduct_model"].sudo().search([("id","=",response["id"])])
            orderdata.sudo().unlink()
            data={  
                "status":200,
                }
            return data
        except Exception as e:
            data={  
                "status":404,
                "error":e 
                }
            return data