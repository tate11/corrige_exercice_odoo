# -*- coding: utf-8 -*-

from odoo import models, fields, api

class SaleOrder(models.Model):
    _inherit = "sale.order"

    is_visible = fields.Boolean(string='Is visible', compute='_add_to_group', default=False)

    @api.depends('state')
    def _add_to_group(self):
        self.is_visible = False
        user_name = self.env.user.has_group('sale_test.group_cancel_confirmed_order')
        if (user_name and (self.state == 'sale')) or (self.state in ('draft', 'sent')):
            self.is_visible = True
        return True
