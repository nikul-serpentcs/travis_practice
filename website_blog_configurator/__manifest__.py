# -*- coding: utf-8 -*-
# Copyright 2018 Serpent Consulting Services Pvt. Ltd.
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

{
    "name": "Website Blog Configurator",
    "version": "10.0.1.0.0",
    "author": "Serpent Consulting Services Pvt. Ltd.",
    'category': 'website',
    "website": "http://www.serpentcs.com",
    "description": """ Website Blog Configurator.""",
    'depends': [
        'website_blog'
    ],
    'data': [
        'views/assets.xml',
        'views/website_blog_configuratoer_view.xml',
        'views/dynamic_blog_carousel.xml',
    ],
    'installable': True,
    'auto_install': False,
}
