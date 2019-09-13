# -*- coding: utf-8 -*-

from odoo import models, fields, api

class DisplayConnectedUser(models.Model):
    _inherit = 'res.users'

    def display_current_user(self):
        context = self._context
        current_uid = context.get('uid')
        # current_user = self.browse(current_uid)
        ir_model_data = self.env['ir.model.data']
        template_form_id = ir_model_data.get_object_reference('base', 'view_users_form')[1]
        context = self._context.copy()
        return {
            'type': 'ir.actions.act_window',
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'res.users',
            'res_id': current_uid,
            'views': [(template_form_id, 'form')],
            'view_id': template_form_id,
            'target': 'current',
            'context': context,
        }
