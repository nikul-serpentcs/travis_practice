# -*- coding: utf-8 -*-
# Copyright 2018 Serpent Consulting Services Pvt. Ltd.
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from odoo import models, fields


class ResCity(models.Model):
    _name = "res.city"

    name = fields.Char(
        string='City Name',
        required=True
    )
    state_id = fields.Many2one(
        'res.country.state',
        string='State',
        required=True
    )
    country_id = fields.Char(
        related='state_id.country_id.name',
        string='Country'
    )
