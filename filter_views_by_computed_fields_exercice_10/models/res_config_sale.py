# -*- coding: utf-8 -*-

from odoo import models, fields, api


class SaleConfiguration(models.TransientModel):
    _inherit = 'sale.config.settings'

    age_setting = fields.Integer(string='Âge')

    @api.multi
    def set_sale_config(self):
        return self.env['ir.values'].sudo().set_default(
            'sale.config.settings', 'age_setting', self.age_setting)
        # icp = self.env['ir.config_parameter']
        # icp.set_param('filter_views_by_computed_fields_exercice_10.age_setting', str(self.age_setting))
        # pass
