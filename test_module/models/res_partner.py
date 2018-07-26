# -*- coding: utf-8 -*-
# Copyright 2018 Serpent Consulting Services Pvt. Ltd.
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from odoo import models, fields, api


class ResPartner(models.Model):
    _inherit = 'res.partner'

    committee_position = fields.Char(
        'Committee position'
    )

    @api.multi
    def write(self, vals):
        vals.update({'committee_position': self.committee_position})
        return super(ResPartner, self).write(vals)
