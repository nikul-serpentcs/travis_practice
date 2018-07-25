# -*- coding: utf-8 -*-
# Copyright 2018 Serpent Consulting Services Pvt. Ltd.
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

{
    'name': 'Places For Community Portal',
    'category': 'website',
    'summary': 'Place management',
    'version': '10.0.1.0.0',
    'license': 'AGPL-3',
    'website': 'www.serpentcs.com',
    'depends': [
        'website_community_portal',
        'web_google_maps'
    ],
    'data': [
        'views/actions.xml',
        'views/assets.xml',
        'views/template_place_detail.xml',
        'views/menu_details.xml',
        'security/portal_security.xml',
        'security/ir.model.access.csv',
        'views/place_view.xml',
        'views/template_place.xml',
        'views/template_select_place.xml',
        'views/template_insert_place.xml',
        'report/report_regi.xml',
        'report/filter_place.xml'
    ],
    'installable': True,
    'application': True,
}
