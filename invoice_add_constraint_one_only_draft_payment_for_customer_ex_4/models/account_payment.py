# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError


class AccountPayment(models.Model):
    _inherit = 'account.payment'

    @api.constrains('state')
    def _check_only_one_draft_payment(self):
        payment_ids = self.search([('partner_id','=',self.partner_id.id), ('state','=','draft'), ('id','!=',self.id)])
        if payment_ids:
            raise ValidationError("Ce client a un paiement à l'état brouillon, vous devez le confirmer avant d'en créer un nouveau.")




