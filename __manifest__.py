{
    'name': 'Custom Module',
    'version': '1.0',
    'category': 'Custom',
    'summary': 'Module for TOdO tasks',
    'description': 'A simple module to manage tasks.',
    'depends': ['base'],
    'data': [
        'views/to_do_task_views.xml',
        'data/email_template_data.xml',
        'data/ir_cron_data.xml',
    ],
    'installable': True,
    'application':True,
}