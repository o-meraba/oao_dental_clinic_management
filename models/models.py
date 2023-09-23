# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class oao_dental-clinic-management(models.Model):
#     _name = 'oao_dental-clinic-management.oao_dental-clinic-management'
#     _description = 'oao_dental-clinic-management.oao_dental-clinic-management'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
