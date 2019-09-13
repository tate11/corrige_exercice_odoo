# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.tools.float_utils import float_compare, float_round, float_is_zero


class Product(models.Model):
    _inherit = 'product.template'

    qty_product = fields.Float(compute="_get_qty_product",)

    def _get_qty_product(self):
        #calculer la somme de la quantite du produit dans les locations de l'entrepôt
        #chercher l'entrepot désiré
        #chercher les locations de cet entrepot
        #calculer la quantite de produit dans tous les locations
        location_obj = self.env['stock.location']
        main_warehouse_id = self.env['stock.warehouse'].search([('main_warehouse','=',True)])
        main_location_id = main_warehouse_id.view_location_id
        child_ids = main_location_id.child_ids.ids
        is_list_edited = True
        while is_list_edited:
            is_list_edited = False
            for child_id in child_ids:
                obj_loc = location_obj.browse(child_id)
                list_child = obj_loc.child_ids.ids
                for ele_child in list_child:
                    if(ele_child not in child_ids):
                        child_ids.append(ele_child)
                        is_list_edited = True
        print('child_ids= ', child_ids)
        total_qty = 0
        for location_child_id in child_ids:
            product_id = self.env['product.product'].search([('id','=',self.id)])
            stock_quant_obj = self.env['stock.quant'].search([('location_id', '=', location_child_id),('product_id','=',product_id.id)])
            for st_quant_id in stock_quant_obj:
                total_qty+=st_quant_id.qty
                print('qty',total_qty)
            self.qty_product = total_qty


    # @api.multi
    # def _compute_quantities_dict(self, lot_id, owner_id, package_id, from_date=False, to_date=False):
    #     main_warehouse_id = self.env['stock.warehouse'].search([('main_warehouse','=',True)]).id
    #     domain_quant_loc, domain_move_in_loc, domain_move_out_loc = self._get_domain_locations()
    #     domain_quant = [('product_id', 'in', self.ids)] + domain_quant_loc
    #     domain_quant += [('warehouse_id', '=', main_warehouse_id)]
    #     return super(Product, self)._compute_quantities_dict(lot_id, owner_id, package_id, from_date=False, to_date=False)


    # @api.multi
    # def _compute_quantities_dict(self, lot_id, owner_id, package_id, from_date=False, to_date=False):
    #     main_warehouse_id = self.env['stock.warehouse'].search([('main_warehouse','=',True)]).id
    #
    #
    #     domain_quant_loc, domain_move_in_loc, domain_move_out_loc = self._get_domain_locations()
    #     domain_quant = [('product_id', 'in', self.ids)] + domain_quant_loc
    #     dates_in_the_past = False
    #     if to_date and to_date < fields.Datetime.now(): #Only to_date as to_date will correspond to qty_available
    #         dates_in_the_past = True
    #
    #     domain_move_in = [('product_id', 'in', self.ids)] + domain_move_in_loc
    #     domain_move_out = [('product_id', 'in', self.ids)] + domain_move_out_loc
    #     if lot_id:
    #         domain_quant += [('lot_id', '=', lot_id)]
    #     if owner_id:
    #         domain_quant += [('owner_id', '=', owner_id)]
    #         domain_move_in += [('restrict_partner_id', '=', owner_id)]
    #         domain_move_out += [('restrict_partner_id', '=', owner_id)]
    #     if package_id:
    #         domain_quant += [('package_id', '=', package_id)]
    #     if dates_in_the_past:
    #         domain_move_in_done = list(domain_move_in)
    #         domain_move_out_done = list(domain_move_out)
    #     if from_date:
    #         domain_move_in += [('date', '>=', from_date)]
    #         domain_move_out += [('date', '>=', from_date)]
    #     if to_date:
    #         domain_move_in += [('date', '<=', to_date)]
    #         domain_move_out += [('date', '<=', to_date)]
    #
    #     Move = self.env['stock.move']
    #     Quant = self.env['stock.quant']
    #     domain_move_in_todo = [('state', 'not in', ('done', 'cancel', 'draft'))] + domain_move_in
    #     domain_move_out_todo = [('state', 'not in', ('done', 'cancel', 'draft'))] + domain_move_out
    #     moves_in_res = dict((item['product_id'][0], item['product_qty']) for item in Move.read_group(domain_move_in_todo, ['product_id', 'product_qty'], ['product_id']))
    #     moves_out_res = dict((item['product_id'][0], item['product_qty']) for item in Move.read_group(domain_move_out_todo, ['product_id', 'product_qty'], ['product_id']))
    #     quants_res = dict((item['product_id'][0], item['qty']) for item in Quant.read_group(domain_quant, ['product_id', 'qty'], ['product_id']))
    #     if dates_in_the_past:
    #         # Calculate the moves that were done before now to calculate back in time (as most questions will be recent ones)
    #         domain_move_in_done = [('state', '=', 'done'), ('date', '>', to_date)] + domain_move_in_done
    #         domain_move_out_done = [('state', '=', 'done'), ('date', '>', to_date)] + domain_move_out_done
    #         moves_in_res_past = dict((item['product_id'][0], item['product_qty']) for item in Move.read_group(domain_move_in_done, ['product_id', 'product_qty'], ['product_id']))
    #         moves_out_res_past = dict((item['product_id'][0], item['product_qty']) for item in Move.read_group(domain_move_out_done, ['product_id', 'product_qty'], ['product_id']))
    #
    #     res = dict()
    #     for product in self.with_context(prefetch_fields=False):
    #         res[product.id] = {}
    #         if dates_in_the_past:
    #             qty_available = quants_res.get(product.id, 0.0) - moves_in_res_past.get(product.id, 0.0) + moves_out_res_past.get(product.id, 0.0)
    #         else:
    #             qty_available = quants_res.get(product.id, 0.0)
    #         res[product.id]['qty_available'] = float_round(qty_available, precision_rounding=product.uom_id.rounding)
    #         res[product.id]['incoming_qty'] = float_round(moves_in_res.get(product.id, 0.0), precision_rounding=product.uom_id.rounding)
    #         res[product.id]['outgoing_qty'] = float_round(moves_out_res.get(product.id, 0.0), precision_rounding=product.uom_id.rounding)
    #         res[product.id]['virtual_available'] = float_round(
    #             qty_available + res[product.id]['incoming_qty'] - res[product.id]['outgoing_qty'],
    #             precision_rounding=product.uom_id.rounding)
    #
    #     return res

