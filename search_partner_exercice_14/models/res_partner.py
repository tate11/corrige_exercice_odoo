# -*- coding: utf-8 -*-

from odoo import models, fields, api
import datetime


class Partner(models.Model):
    _inherit = 'res.partner'

    @api.model
    def cron_list_partner(self):
        print("Cron partner")
        three_year_ago_date = datetime.datetime.now() - datetime.timedelta(days=3 * 365)
        #list des partenaires qui  qui n'ont pas de parent, qui sont client
        partner_obj = self.search([('parent_id', '=', False), ('customer', '=', True), ('create_date', '<', str(three_year_ago_date) )])
        print('partner_obj', partner_obj)
        for partner in partner_obj:
            disable_partner = True
            invoice_ids = partner.invoice_ids
            print('date now', datetime.datetime.now())
            for invoice in invoice_ids:
                # au moins il existe une seul date de creation de facture > 3 ans
                if (invoice.create_date > str(three_year_ago_date)):
                    disable_partner = False
                    break
            if(disable_partner):
                partner.active = False

            # for invoice in invoice_ids:
            #     date_diff = datetime.datetime.now() - invoice.create_date
            #     if invoice.date_invoice < str(three_year_ago_date):
            #         self._cr.execute("""
            #                                 SELECT distinct(id)
            #                                 FROM account_invoice
            #                                 WHERE (%s>=%s)
            #                                 AND id NOT IN (
            #                                                 SELECT id
            #                                                 FROM account_invoice
            #                                                 WHERE %s <%s)
            #
            #                                  """, (date_diff, three_year_ago_date, date_diff, three_year_ago_date))
            # # rec.active = False





