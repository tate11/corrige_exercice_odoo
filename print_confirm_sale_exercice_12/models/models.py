# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError

class SaleOrder(models.Model):
    _inherit = "sale.order"

    @api.multi
    def print_quotation(self):
        self.filtered(lambda s: s.state == 'draft').write({'state': 'sent'})
        if self.state == 'sale':
            return self.env['report'].get_action(self, 'sale.report_saleorder')
        else:
            raise ValidationError('Sale order must be confirmed!')


class SaleOrderReportConfirmed(models.AbstractModel):
    _name = 'report.sale.report_saleorder'

    @api.model
    def render_html(self, docids, data=None):
        sale_order_id = self.env['sale.order'].browse(docids)
        if sale_order_id.state == 'sale':
            docargs = {
                'doc_ids': docids,
                'doc_model': 'sale.order',
                'docs': sale_order_id,
                'data': data,
            }
            return self.env['report'].render('sale.report_saleorder', docargs)
        else:
            raise ValidationError('Sale order must be confirmed!qqqqqqqqq')

