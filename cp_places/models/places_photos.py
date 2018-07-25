# -*- coding: utf-8 -*-
# Copyright 2018 Serpent Consulting Services Pvt. Ltd.
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from odoo import models, fields


class PlacesPhotos(models.Model):
    _name = 'places.photos'

    name = fields.Binary(string="Add image")
    place_id = fields.Many2one(
        'places.place',
        string='Place'
    )
