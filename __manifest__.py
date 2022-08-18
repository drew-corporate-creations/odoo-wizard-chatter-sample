{
    'name': 'sample',
    'depends': [
        'base',
        'mail'
    ],
    'application': True,
    'data': [
        'views/sample_model_views.xml',
        'security/ir.model.access.csv',
        'wizard/sample_status_wizard_views.xml'
    ]
}
