# -*- coding: utf-8 -*-

from odoo import api, fields, models
from odoo.exceptions import ValidationError


class Partner(models.Model):

    _inherit = 'res.partner'

    age = fields.Integer(string='Age')
    age_config = fields.Integer(compute='_get_age')
    # is_age_visible = fields.Integer(default='')
    # other_age = fields.Integer(string='Age2')
    #
    # _sql_constraints = [
    #    ('other_age_check', 'CHECK(other_age > 18)', 'Error! too young partner! your age must be older then 18')
    # ]

    other_age = fields.Integer('Interval Value', default=20)

    _sql_constraints = [
        ('interval_other_age', 'CHECK(other_age > 18)', 'your age must be older then 18')
    ]

    @api.one
    def _get_age(self):
        self.age_config = self.env['ir.values'].get_default('sale.config.settings', 'age_setting')
        pass

    @api.constrains('age', 'age_config')
    def compute_age_partner(self):
        if self.age < self.age_config:
            raise ValidationError("L'âge de partner doit être supérieur à L'âge dans configuration!")

    # @api.constrains('other_age')
    # def _check_other_age(self):
    #     for record in self:
    #         if record.other_age < 18:
    #             raise ValidationError("too young partner! your age must be older then 18")

