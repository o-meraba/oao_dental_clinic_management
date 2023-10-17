# -*- coding: utf-8 -*-

from odoo import models, fields, api


class DiseaseCategory(models.Model):
    _name = "disease.category"
    _description = "Disease Category"

    name = fields.Char(string="Disease Category Name")