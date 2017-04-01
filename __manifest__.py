{
    'name': 'Customer Sales',
    'version': '1.0',
    'category': 'Tests',
    'summary': 'Customer Sale Relation',
    'website': 'https://www.emiprotechnologies.com',
    'description': """Tests of first""",
    'maintainer': 'OpenERP SA',
    'depends': ['base','stock','sale'],
    
    'data': [
            'views/customer_sale_rel_view.xml',
            'views/customer_sale_rel_action.xml',
            'security/ir.model.access.csv',
            ],
             
    'installable': True,
    'auto_install': False,
}