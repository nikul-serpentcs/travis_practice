# -*- coding: utf-8 -*-
# Copyright 2018 Serpent Consulting Services Pvt. Ltd.
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from odoo import http
from odoo.http import request


class WebsiteCommittees(http.Controller):
    @http.route(['/page/committee'], type='http', auth="public",
                method=['post'], website=True, csrf=False)
    def show_committee_page(self, page=0, ppg=False, **post):
        job_pos_data = request.env['job.position'].search([])
        res_partner = request.env['res.partner'].search([])
        vals = {
            'job_positions': job_pos_data,
            'res_partner': res_partner
        }
        return request.render('cp_committee.template_committee_chart', vals)

    @http.route(['/page/committee/list'], type='http', auth="public",
                method=['post'], website=True, csrf=False)
    def show_committee_page_grid(self, page=0, ppg=False, **post):
        job_pos_data = request.env['job.position'].search([])

        vals = {
            'job_pos_data': job_pos_data
        }
        return request.render('cp_committee.template_committee_grid', vals)
