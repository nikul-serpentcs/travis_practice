# -*- coding: utf-8 -*-
# Copyright 2018 Serpent Consulting Services Pvt. Ltd.
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

{
    'name': 'Website Portal Enhanced',
    'category': 'Website',
    'summary': 'Account Management Frontend for your Customers',
    'version': '10.0.1.0.0',
    'license': 'AGPL-3',
    'author': 'Serpent Consulting Services PVT. LTD.',
    'website': 'http://www.serpentcs.com',
    'depends': [
        'website_portal'
    ],
    'data': [
        'views/assets.xml',
        'views/my_account_inherited_view.xml',
        'views/portal_details_inherited_view.xml'
    ],
    'installable': True,
    'application': True
}
