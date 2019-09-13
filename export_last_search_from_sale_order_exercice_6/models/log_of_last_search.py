# -*- coding: utf-8 -*-

from odoo import models, fields, api, _

class LogSearch(models.Model):
    _name = 'log.search'

    name = fields.Char(string='name')
    user_id = fields.Char()
    domain_search = fields.Char()

    sale_log_search = fields.Many2many('sale.order', 'sale_order_log_search_rel', 'log_search_id', 'sale_order_id',
                                     string='Sales Search')