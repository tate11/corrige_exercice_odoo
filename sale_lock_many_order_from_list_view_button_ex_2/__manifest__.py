# -*- coding: utf-8 -*-
{
    'name': "sale_lock_many_order_from_list_view_button",

    'summary': """
       Lock many order from list view""",

    'description': """
       In the list of sales orders, add a sub-menu under the Action menu, which allows you to lock multiple commands at once
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','sale'],

    # always loaded
    'data': [
        'data/sale_data.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
    ],
}