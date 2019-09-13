# -*- coding: utf-8 -*-

from odoo import models, fields, api, _

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    # def default_get(self):
    #     print('Hello')

    # result_domain_search = fields.Char(compute='')

    @api.model
    def search(self, args, offset=0, limit=None, order=None, count=False):
        res = super(SaleOrder, self).search(args, offset, limit, order, count=count)
        vals = {
                'user_id': self.user_id.id,
                'sale_log_search': [[6, False, [res.ids]]],
                'name': str(res)
        }
        self.env['log.search'].create(vals)
        return res


    @api.multi
    def open_wizard(self):
        print("call wizard function 1")
        # self.ensure_one()
        return {
            'name': _('Export last search'),
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'export.last.search.wizard',
            'view_id': self.env.ref('wizard_export_last_search').id,
            'type': 'ir.actions.act_window',
            'target': 'new',
        }
