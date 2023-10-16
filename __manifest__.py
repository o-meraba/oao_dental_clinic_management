# -*- coding: utf-8 -*-
{
    'name': "Dental Clinic Management",

    'summary': """
         This app is used in Dental Clinic for management
         
         """,

    'description': """
       This app includes patient information, appointments, treatments etc.
    """,

    'author': "Omer ABA",
    'website': "http://www.omeraba.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Management',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
         'views/menu.xml',
        'views/dental_patients_view.xml',
        'views/dental_appointment_view.xml',
        'views/dental_center_view.xml',
        'views/dental_room_view.xml',
        'views/dentist_view.xml',
       
    ],
    'installable': True,
    'application': True,
    'sequence':-100,
}
