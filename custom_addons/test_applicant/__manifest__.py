{
    "name": "Test Applicant",
    "author": "Aleksandar Markovic",
    "license": "AGPL-3",
    "version": "0.1",
    "category": "Test",
    "summary": "Test Applicant",
    'depends': ['base'],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/test_applicant_views.xml',
        'views/menu.xml',
    ],
    'installable': True,
    'application': True,
}