# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError


class Picking(models.Model):
    _inherit = "stock.picking"

    def merge_delivery(self):
        picking_ids = self.browse(self.env.context['active_ids'])
        move_lines = []
        first_picking = picking_ids[0]
        for picking in picking_ids:
            if (picking.state != first_picking.state or picking.partner_id != first_picking.partner_id):
                raise ValidationError("All deliveries must have same partner with same state!")
            elif (picking.state == first_picking.state and picking.partner_id == first_picking.partner_id):
                print('same state and same partner')
                for move in picking.move_lines:
                    #Les lignes de livraison seront fusionnées si elles ont le même produit,
                    # le même emplacement source, le même emplacement de destination et la même unité de mesure.
                    # Sinon, ils seront affiché sous la livraison fusionnée mais de manière séparée.

                    move_lines.append((0, 0, {'name': '/',
                        'product_id': move.product_id.id,
                        'product_uom': move.product_uom.id,
                        'product_uom_qty': move.product_uom_qty,
                        'location_id': move.location_id.id,
                        'location_dest_id': move.location_dest_id.id,
                        'state': move.state,
                    }))
                move_lines = move_lines
                result_lines = []

                for line in move_lines:
                    edit_line = False
                    for res_line in result_lines:
                        if (res_line[2]['product_id'] == line[2]['product_id']) and \
                                (res_line[2]['product_uom'] == line[2]['product_uom']) and \
                                (res_line[2]['location_dest_id'] == line[2]['location_dest_id']) and \
                                (res_line[2]['location_id'] == line[2]['location_id']):
                            res_line[2]['product_uom_qty'] += line[2]['product_uom_qty']
                            edit_line = True

                    if not edit_line:
                        result_lines.append(line)

                vals = {
                    'name':'/',
                    'partner_id': picking.partner_id.id,
                    'picking_type_id': picking.picking_type_id.id,
                    'location_id': picking.location_id.id,
                    'location_dest_id': picking.location_dest_id.id,
                    'state': picking.state,
                    'move_lines': result_lines
                }
        pick_merged = self.create(vals)
        pick_canceled = picking_ids.action_cancel()
