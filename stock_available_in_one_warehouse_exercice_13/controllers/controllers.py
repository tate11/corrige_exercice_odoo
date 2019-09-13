# -*- coding: utf-8 -*-
from odoo import http

# class StockAvailableInOneWarehouse(http.Controller):
#     @http.route('/stock_available_in_one_warehouse/stock_available_in_one_warehouse/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/stock_available_in_one_warehouse/stock_available_in_one_warehouse/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('stock_available_in_one_warehouse.listing', {
#             'root': '/stock_available_in_one_warehouse/stock_available_in_one_warehouse',
#             'objects': http.request.env['stock_available_in_one_warehouse.stock_available_in_one_warehouse'].search([]),
#         })

#     @http.route('/stock_available_in_one_warehouse/stock_available_in_one_warehouse/objects/<model("stock_available_in_one_warehouse.stock_available_in_one_warehouse"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('stock_available_in_one_warehouse.object', {
#             'object': obj
#         })