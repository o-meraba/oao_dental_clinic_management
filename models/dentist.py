# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Dentist(models.Model):
    _name = "dentist"
    _description = "Dentist"

    name = fields.Char(string="Dentist Name", tracking=True)
    surname = fields.Char(string="Dentist Surname", tracking=True)
    phone = fields.Char(string="Phone", tracking=120)
    dental_clinic_center = fields.Char(string="Dental Clinic Center")
    note = fields.Text(string="Description", tracking=True)
