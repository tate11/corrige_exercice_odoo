# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.tools import DEFAULT_SERVER_DATETIME_FORMAT, float_compare

class StockWarehouse(models.Model):
    _inherit = "stock.warehouse"

    main_warehouse = fields.Boolean(string="Main Warehouse", default=False)

# class SaleOrderLine(models.Model):
#     _inherit = 'sale.order.line'
#
#     @api.onchange('product_uom_qty', 'product_uom', 'route_id')
#     def _onchange_product_id_check_availability(self):
#
#         if not self.product_id or not self.product_uom_qty or not self.product_uom:
#             self.product_packaging = False
#             return {}
#         if self.product_id.type == 'product':
#             precision = self.env['decimal.precision'].precision_get('Product Unit of Measure')
#             product_qty = self.product_uom._compute_quantity(self.product_uom_qty, self.product_id.uom_id)
#             if float_compare(self.product_id.virtual_available, product_qty, precision_digits=precision) == -1:
#                 is_available = self._check_routing()
#                 if not is_available:
#                     warning_mess = {
#                         'title': _('Not enough inventory!'),
#                         'message': _(
#                             'You plan to sell %s %s but you only have %s %s available!\nThe stock on hand is %s %s.') % \
#                                    (self.product_uom_qty, self.product_uom.name, self.product_id.virtual_available,
#                                     self.product_id.uom_id.name, self.product_id.qty_available,
#                                     self.product_id.uom_id.name)
#                     }
#                     return {'warning': warning_mess}
#             else:
#                 print("available")
#                 company = self.env.user.company_id.id
#                 warehouse_id = self.env['stock.warehouse'].search([('company_id', '=', company)], limit=1)
#                 # stock_warehouse_obj = self.env['stock.warehouse'].search([('id', '=', warehouse_id.id)])
#                 print("stock_warehouse_obj", warehouse_id.main_warehouse)
#         return {}