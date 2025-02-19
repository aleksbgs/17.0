{
    "name": "Test Applicant",
    "author": "Aleksandar Markovic",
    "license": "AGPL-3",
    "version": "0.1",
    "category": "Test",
    "summary": "Test Applicant",
    'depends': ['base','web'],
    'data': [
        'views/res_users_views.xml',
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/test_applicant_views.xml',
        'views/menu.xml',
    ],
    'installable': True,
    'application': True,
    'assets': {
        'web.assets_backend': [
            'test_applicant/static/src/js/login_as_user.js',
        ],
    },

}