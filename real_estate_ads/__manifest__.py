{
    "name": "Real estate ads",
    "version": "1.0",
    "author": "Nirav",
    "description" """
           Real estate module to show available properties 111111"""
    "category": "Sales",
    "depends": ['base'],
    "data": [
        'security/ir.model.access.csv',
        'views/property_view.xml',
        'views/property_type_view.xml',
        'views/menu_items.xml',
    ],
    "installable": True,
    "application": True,
    "license": "LGPL-3",
}