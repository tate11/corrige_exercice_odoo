# -*- coding: utf-8 -*-

from odoo import models, fields, api


import odoo.addons.decimal_precision as dp

class LikeSaleLine(models.Model):
    _name = 'like.sale.line'


    price_unit = fields.Float('Unit Price', required=True, digits=dp.get_precision('Product Price'), default=0.0)
    # price_subtotal = fields.Monetary(compute='_compute_amount', string='Subtotal', readonly=True, store=True)
    price_tax = fields.Monetary(compute='_compute_amount', string='Taxes', readonly=True, store=True)
    price_total = fields.Monetary(compute='_compute_amount', string='Total', readonly=True, store=True)
    tax_id = fields.Many2many('account.tax', string='Taxes', domain=['|', ('active', '=', False), ('active', '=', True)])
    discount = fields.Float(string='Discount (%)', digits=dp.get_precision('Discount'), default=0.0)
    product_id = fields.Many2one('product.product', string='Product', domain=[('sale_ok', '=', True)], change_default=True, ondelete='restrict', required=True)
    product_uom_qty = fields.Float(string='Quantity', digits=dp.get_precision('Product Unit of Measure'), required=True, default=1.0)
    product_uom = fields.Many2one('product.uom', string='Unit of Measure', required=True)
    currency_id = fields.Many2one('res.currency', string='Currency', default=lambda self: self.env.user.company_id.currency_id)
    company_id = fields.Many2one('res.company', string='Company')
    tax_total = fields.Monetary(compute='_compute_taxes', string='Total Taxes', readonly=True, store=True)


    @api.depends('product_uom_qty', 'discount', 'price_unit', 'tax_id')
    def _compute_amount(self):
        price = self.price_unit * (1 - (self.discount or 0.0) / 100.0)
        taxes = self.tax_id.compute_all(price, self.currency_id, self.product_uom_qty,
                                        product=self.product_id, partner=None)
        self.price_tax = taxes['total_included'] - taxes['total_excluded']
        self.price_total = taxes['total_included']
        # self.price_subtotal = taxes['total_excluded']
