# -*- coding: utf-8 -*-
# Copyright 2018 Serpent Consulting Services Pvt. Ltd.
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

{
    'name': 'Event For Community Portal',
    'category': 'Website',
    'summary': 'Event Management',
    'version': '10.0.1.0.0',
    'license': 'AGPL-3',
    'website': 'www.serpentcs.com',
    'depends': [
        'event',
        'website_community_portal',
    ],
    'external_dependencies': {
        'python': ['xlrd']
    },
    'data': [
        'wizard/event_attendees_views.xml',
        'views/view_events.xml',
    ],
    'installable': True,
    'application': True,
}
