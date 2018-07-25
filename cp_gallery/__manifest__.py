# -*- coding: utf-8 -*-
# Copyright 2018 Serpent Consulting Services Pvt. Ltd.
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

{
    'name': 'Gallery For Community Portal',
    'category': 'website',
    'summary': 'Gallery management',
    'version': '10.0.1.0.0',
    'license': 'AGPL-3',
    'website': 'www.serpentcs.com',
    'depends': [
        'cp_event',
    ],
    'data': [
        'views/assets.xml',
        'views/gallery_view.xml',
        'views/menu_details.xml',
        'views/template_list_events.xml',
        'views/template_show_event_photos.xml'
    ],
    'installable': True,
    'application': True,
}
