# -*- coding: utf-8 -*-

from odoo import models, fields, api


class DentalCenter(models.Model):
    _name = "dental.center"
    _description = "Dental Center"
    _order = 'name desc'

    name = fields.Char(string="Center Name")
    code = fields.Integer(string="Center Code")
    administrator = fields.Char(string="Center Administrator")
    address = fields.Char(string="Center Address")
    