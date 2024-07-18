# -*- coding: utf-8 -*-

{
    'name': 'Custom Sales',
    'version': '1.1',
    'summary': 'Customizations for Sales module',
    'description': 'This module adds Custom fields and actions to the Sales Module.',
    'author': 'Shuaib Zaman',
    'category': 'Sales',
    'depends': ['sale'],
    'data': [
        'views/sale_order_views.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}
