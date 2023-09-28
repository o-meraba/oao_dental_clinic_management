# -*- coding: utf-8 -*-

from odoo import models, fields, api


class DentalPatients(models.Model):
    _name = "dental.patients"
    _description = "Dental Patients"
    _order = 'name desc'

    name = fields.Char(string="Patient Name", tracking=True)
    surname = fields.Char(string="Patient Surname", tracking=True)
    date_of_birth = fields.Date("Date Of Birth", tracking=30)
    age = fields.Integer(string="Patient Age")
    patient_id = fields.Char(string="Patient ID")
    image = fields.Image(string="Image")
    gender = fields.Selection([('male', "Male"), ('female', 'Female')], string='Gender', default='male')
    note = fields.Text(string="Description", tracking=True)
    phone = fields.Char(string="Phone", tracking=120)
    email = fields.Char(string="Email")
