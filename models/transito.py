from odoo import fields, models, api
class ProductosTransito(models.Model):
    _name ='ventas.transito'
    _description = 'Ventas en lista de transito'

    cant_disponible = fields.Integer('cant_disp')
    medidas = fields.Char('medidas')
    modelo = fields.Char('modelo')
    lonas = fields.Char('lonas')
    marca = fields.Char('marca')

    precio_dolar_uno = fields.Float('precio_dolar_uno')
    precio_bolivar_uno = fields.Float('precio_bolivar_uno')

    precio_dolar_dos = fields.Float('precio_dolar_dos')
    precio_bolivar_dos = fields.Float('precio_bolivar_dos')

    precio_dolar_tres = fields.Float('precio_dolar_tres')
    precio_bolivar_tres = fields.Float('precio_bolivar_tres')

    imagen = fields.Binary()

    titulo_producto = fields.Char('Titulo del reporte')

    def _transitoProductos(self):
        busqueda = self.env['ventas.transito'].search([
            ('estado', '=', 'transito')
        ])
        self.datos = busqueda