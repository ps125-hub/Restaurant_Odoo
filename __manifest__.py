# -*- coding: utf-8 -*-
{
    'name': "restaurant_app",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Peisen Dong",
    'website': "http://www.isca.es",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/category_view.xml',
        'views/product_view.xml',
        'views/ingredients_view.xml',
        "views/order_view.xml",
        "views/lineProduct_view.xml",
        "views/invoice_view.xml",
        'views/menu.xml',
        #'views/views.xml',

    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'application':True,
    'installable':True,
}
