# -*- coding: utf-8 -*-
# Copyright 2018 Serpent Consulting Services Pvt. Ltd.
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from odoo import models, api


class ResUser(models.Model):
    _inherit = 'res.users'

    @api.model
    def create(self, vals):
        vals['active'] = False
        return super(ResUser, self).create(vals)

    @api.multi
    def write(self, vals):
        if self.active:
            self.partner_id.active = False
        else:
            self.partner_id.active = True
        return super(ResUser, self).write(vals)
