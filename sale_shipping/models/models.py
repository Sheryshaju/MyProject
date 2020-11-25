# -*- coding: utf-8 -*-
from odoo import models, fields

class SaleOrder(models.Model):
	_inherit = 'sale.order'
	ship = fields.Many2one('sales.ship',string="ship",required=True)

   

class SaleShip(models.Model):


    _name = "sales.ship"
    name = fields.Char(string='Name', required=True)
    IMO = fields.Char('IMO', size=64, required=True)
    hull_number = fields.Char('Hull Number', size=64, required=True)
    engine_number = fields.Char('Engine Number', size=64, required=True)
    vessel_name = fields.Char('Vessel Name', size=64, required=True)
    build_year = fields.Date('Build Year', required=True)
    ship_yard = fields.Many2one('res.partner', 'Ship Yard')
    ship_owner = fields.Many2one('res.partner', 'Ship Owner')
    ship_management = fields.Many2one('res.partner', 'Ship Management')
    engine_builder = fields.Many2one('res.partner', 'Engine Builder')
