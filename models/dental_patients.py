# -*- coding: utf-8 -*-

from odoo import models, fields, api


class DentalPatients(models.Model):
    _name = "dental.patients"
    _description = "Dental Patients"
    _order = 'name desc'

    name = fields.Char(string="Patient Name", tracking=True)
    surname = fields.Char(string="Patient Surname", tracking=True)