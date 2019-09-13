# -*- coding: utf-8 -*-
{
    'name': "export_last_search_from_sale_order",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['sale'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        # 'data/export_last_search_button.xml',
        'views/export_last_search_button_view.xml',
        # 'views/sale_order_view.xml',
        # 'views/views.xml',
        'wizards/wizard_export_last_search.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
    ],
}