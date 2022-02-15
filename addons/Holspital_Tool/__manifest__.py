# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': "Holspital Tool",
    'version': '1.0',
    'category': 'Extra Tools',
    'summary': "Modulo de emplo, para el aprendizaje de odoo",
    'description': "Modulo orientado al control de un hospital.",
    'sequence': '10',
    'license': 'LGPL-3',
    'author': 'Pascual Neftalí Chávez Campos',
    'website': 'https://soluciones.tekniu.mx/',
    'depends': ['sale'],
    'demo': [],
    'data': [
        "security/security.xml",
        "security/ir.model.access.csv",
        "data/sequence_data_patients.xml",
        "data/sequence_data_appointments.xml",
        "views/patient.xml",
        "views/appointment.xml",
        "views/sale.xml",
        "report/report.xml",
        "report/report_patient_resume.xml"
        ],
    'installable': True,
    'Application': True,
    'Auto_install': True,
}