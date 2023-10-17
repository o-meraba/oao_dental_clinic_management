# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Disease(models.Model):
    _name = "disease"
    _description = "Disease"

    name = fields.Char(string="Disease Name")
    code = fields.Char(string="Disease Code")
    category = fields.Char(string="Disease Category")