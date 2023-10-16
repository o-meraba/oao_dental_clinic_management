# -*- coding: utf-8 -*-

from odoo import models, fields, api


class DentalAppointment(models.Model):
    _name = "dental.appointment"
    _description = "Dental Appointment"

    patient_name = fields.Char(string="Patient Name", tracking=True) #todo many2one olarak yapılacak
    patient_surname = fields.Char(string="Patient Surname", tracking=True) #todo many2one olarak yapılacak
    appointment_id = fields.Char(string="Patient ID")
    phone = fields.Char(string="Phone Number", tracking=120)
    urgency_level = fields.Integer(string="Urgency Level")
    appointment_start_time = fields.Date(string="Appointment Start Time")
    dentist = fields.Char(string="Dentist") #todo many2one olarak yapılacak
    dental_clinic_center = fields.Char(string="Dental Clinic Center") #todo many2one olarak yapılacak
    note = fields.Text(string="Description", tracking=True)
    appointment_request = fields.Char(string="Appointment Request")

