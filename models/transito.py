from odoo import fields, models, api
class ProductosTransito(models.Model):
    _inherit = 'ventas.disp'

    def _disponiblesProductos(self):
        busqueda = self.env['ventas.disp'].search([
            ('estado', '=', 'transito')
        ])
        self.datos = busqueda
