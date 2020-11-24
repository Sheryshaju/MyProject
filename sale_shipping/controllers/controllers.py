# -*- coding: utf-8 -*-
# from odoo import http


# class SaleShipping(http.Controller):
#     @http.route('/sale_shipping/sale_shipping/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/sale_shipping/sale_shipping/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('sale_shipping.listing', {
#             'root': '/sale_shipping/sale_shipping',
#             'objects': http.request.env['sale_shipping.sale_shipping'].search([]),
#         })

#     @http.route('/sale_shipping/sale_shipping/objects/<model("sale_shipping.sale_shipping"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('sale_shipping.object', {
#             'object': obj
#         })
