from odoo import models, fields

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    seller = fields.Char(
    	string='Sales Rep',
    	store=True,
    	default='Shuaib Zaman')
