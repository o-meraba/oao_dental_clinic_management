# -*- coding: utf-8 -*-

from odoo import models, fields, api


class DentalRoom(models.Model):
    _name = "dental.room"
    _description = "Dental Room"
    _order = 'name desc'

    name = fields.Char(string="Room Name")
    code = fields.Integer(string="Room Code")
    dentist = fields.Char(string="Room's Dentist")
    center_name = fields.Char(string="Center Name")
    