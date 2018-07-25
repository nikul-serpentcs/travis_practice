# -*- coding: utf-8 -*-
# Copyright 2018 Serpent Consulting Services Pvt. Ltd.
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from odoo import http
from odoo.http import request


class WebsiteGallery(http.Controller):
    @http.route(['/page/gallery'], type='http', auth="public",
                method=['post'], website=True, csrf=False)
    def show_gallery_page(self, page=0, ppg=False, **post):
        gallery_data = request.env['gallery.gallery'].search([])
        vals = {
            'gallery_data': gallery_data
        }
        return request.render('cp_gallery.template_list_events', vals)

    @http.route(['/page/show_photos'], type='http', auth="public",
                method=['post'], website=True, csrf=False)
    def show_photos_page(self, page=0, ppg=False, **post):
        gallery_photos = request.env['gallery.gallery'].search(
            [('event_id', '=',
              post.get('id'))])
        vals = {
            'gallery_photos': gallery_photos,
            'name': post.get('id')
        }
        return request.render('cp_gallery.template_show_event_photos', vals)
