# -*- coding: utf-8 -*-
# from odoo import http


# class OaoDental-clinic-management(http.Controller):
#     @http.route('/oao_dental-clinic-management/oao_dental-clinic-management', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/oao_dental-clinic-management/oao_dental-clinic-management/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('oao_dental-clinic-management.listing', {
#             'root': '/oao_dental-clinic-management/oao_dental-clinic-management',
#             'objects': http.request.env['oao_dental-clinic-management.oao_dental-clinic-management'].search([]),
#         })

#     @http.route('/oao_dental-clinic-management/oao_dental-clinic-management/objects/<model("oao_dental-clinic-management.oao_dental-clinic-management"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('oao_dental-clinic-management.object', {
#             'object': obj
#         })
