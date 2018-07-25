# -*- coding: utf-8 -*-
# Copyright 2018 Serpent Consulting Services Pvt. Ltd.
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).
from odoo import models, fields


class GalleryPhotos(models.Model):
    _name = 'gallery.gallery'
    _description = 'Stores community photos'
    _rec_name = 'event_id'

    event_id = fields.Many2one(
        'event.event',
        'Event',
    )
    photo_ids = fields.One2many(
        'gallery.photos',
        'gallery_id',
        'Photos',
    )
