from odoo import fields, models, api

class SuperCauchosVentas(models.Model):
    _name = 'ventas.disp'
    _description = 'Ventas lista de productos'

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

    estado = fields.Selection(selection=[('activo', 'Activo'), ('inactivo', 'Inactivo'), ('transito', 'En transito')], default="activo")

    imagen = fields.Binary()

    titulo_producto = fields.Char('Titulo del reporte')
