# -*- coding: utf-8 -*-
{
    'name': 'Accounting Enhancement',

    'version': '17.0',

    'category': 'accounting',

    'website': "https://mycompany.net",
    'license': 'OPL-1',

    'author': "tarek-alhayw",

    'summary': '''
        Account Enhancement Edits
    ''',

    'depends': ['base', 'sale', 'product', 'stock', 'account'],

    'data': [
        'security/ir.model.access.csv',
        'views/assets_category_view.xml',
    ],

}