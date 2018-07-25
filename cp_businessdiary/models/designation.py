# -*- coding: utf-8 -*-
# Copyright 2018 Serpent Consulting Services Pvt. Ltd.
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from odoo import models, fields


class Designations(models.Model):
    _name = 'designations'
    _description = 'Designations'
    _rec_name = 'name'

    name = fields.Char('Designation Name')
    code = fields.Char('Designation Code')
