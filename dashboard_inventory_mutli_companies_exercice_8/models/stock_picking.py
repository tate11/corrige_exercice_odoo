# -*- coding: utf-8 -*-

from odoo import models, fields, api

class PickingType(models.Model):
    _inherit = 'stock.picking.type'


    @api.model
    def search(self, args, offset=0, limit=None, order=None, count=False):
        context = self._context or {}
        current_uid = self.env['res.users']._context.get('uid')
        current_user = self.env['res.users'].browse(current_uid)
        if context.get('stock_company_id'):
            print('1')
            args += [('warehouse_id.company_id', '=', current_user.company_id.id)]
        return super(PickingType, self).search(args, offset, limit, order, count=count)
