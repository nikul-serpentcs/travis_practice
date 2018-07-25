# -*- coding: utf-8 -*-
# Copyright 2018 Serpent Consulting Services Pvt. Ltd.
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).
from odoo import models, fields


class Gallery(models.Model):
    _name = 'gallery.photos'
    _description = 'Stores community photos'

    gallery_id = fields.Many2one(
        'gallery.gallery',
        'Gallery',
    )
    images = fields.Binary(string='Photos')
