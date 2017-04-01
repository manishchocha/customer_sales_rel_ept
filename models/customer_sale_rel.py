from odoo import models,fields,api

class customer_sale_relation(models.Model):
    _name='customer.sale.rel.ept'
    _inherit = ['mail.thread', 'ir.needaction_mixin']
    
    date=fields.Date(string="Date", default=fields.Datetime.now('ddmmyy'))
    sale_order=fields.Many2one("sale.order", string="Sales Order")
    customer=fields.Many2one('res.partner', string="Customer",readonly=True,compute="_value_onchange")
    warehouse=fields.Many2one('stock.warehouse', string="Warehouse",readonly=True,compute="_value_onchange")
    invoice_paid_amount=fields.Float(string="Invoice Paid Amount",readonly=True,compute="_value_onchange")
    invoice_remaining_amount=fields.Float(string="Invoice Remaining Amount",readonly=True,compute="_value_onchange")
    products=fields.Many2many("sale.order.line", string="Order Lines")
       
    @api.multi
    def getProducts(self):
        for record in self:
            record.products = record.sale_order.order_line
            record.name = record.sale_order.name     
            
    @api.depends('sale_order')    
    def _value_onchange(self):
            
        for order in self:
            order.name = order.sale_order.name
            order.customer = order.sale_order.partner_id
            order.warehouse = order.sale_order.warehouse_id
            
            if order.sale_order.invoice_ids.id == False:
                order.invoice_paid_amount = 0.0
                order.invoice_remaining_amount=order.sale_order.amount_total
            else:
                for inv in order.sale_order.invoice_ids:
                    order.invoice_paid_amount = inv.amount_total - inv.residual
                    order.invoice_remaining_amount=inv.residual
    
            order.update({
                    'customer': order.customer,
                    'warehouse':order.warehouse,
                    'invoice_paid_amount':order.invoice_paid_amount,
                    'invoice_remaining_amount':order.invoice_remaining_amount   
                })
