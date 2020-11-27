# -*- coding: utf-8 -*-
from odoo import models, fields


class SaleOrder(models.Model):
    _inherit = 'sale.order'
    ship = fields.Many2one('sales.ship', string="ship", required=True)

    def update_to_order(self):
        sale_order_rec = self.ensure_one()
        for order_line_rec in sale_order_rec.order_line:
            order_line_rec.write({'ship': sale_order_rec.ship.id})


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'
    ship = fields.Many2one('sales.ship', string="Ship")


class SaleOrderTree(models.Model):
    _inherit = 'sale.order'
    ship = fields.Many2one('sales.ship', string="Ship")


class SaleShip(models.Model):
    _name = "sales.ship"
    _sql_constraints = [
        ('IMO_unique', 'unique(IMO)', 'imo number must be unique!'),
    ]

    IMO = fields.Char('IMO', size=64, required=True)
    _rec_name = 'IMO'
    hull_number = fields.Char('Hull Number', size=64, required=True)
    engine_number = fields.Char('Engine Number', size=64)
    vessel_name = fields.Char('Vessel Name', size=64)
    build_year = fields.Date('Build Year')
    ship_yard = fields.Many2one('res.partner', 'Ship Yard')
    ship_owner = fields.Many2one('res.partner', 'Ship Owner')
    ship_management = fields.Many2one('res.partner', 'Ship Management')
    engine_builder = fields.Many2one('res.partner', 'Engine Builder')
