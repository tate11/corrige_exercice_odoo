# -*- coding: utf-8 -*-

from odoo import models, fields, api


class SearchWizard(models.TransientModel):
    _name = "export.last.search.wizard"

    name = fields.Text('Name', readonly=True)

    @api.model
    def default_get(self, fields):
        res = super(SearchWizard, self).default_get(fields)
        log_search_obj = self.env['log.search'].search([], order="id desc", limit=1)
        # print('log_search_obj', log_search_obj)
        # print('sale_log_search', log_search_obj.sale_log_search)
        result = ''
        for rec in log_search_obj.sale_log_search:
            result = result + ',' + rec.name
            res = {
                'name': result,
            }
        return res

