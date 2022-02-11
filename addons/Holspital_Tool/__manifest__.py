# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': "Holspital Tool",
    'version': '1.0',
    'category': 'Extra Tools',
    'summary': "Use python code",
    'description': "This text is only for tesiting.",
    'sequence': '10',
    'license': 'LGPL-3',
    'author': 'Pascual Chavez',
    'website': 'odoomates.com',
    'depends': [],
    'demo': [],
    'data': [
        "security/security.xml",
        "security/ir.model.access.csv",
        "data/sequence_data_patients.xml",
        "data/sequence_data_appointments.xml",
        "views/patient.xml",
        "views/appointment.xml",
        "report/report.xml",
        "report/report_patient_resume.xml"
        ],
    'installable': True,
    'Application': True,
    'Auto_install': True,
}