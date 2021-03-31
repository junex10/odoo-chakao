from odoo import fields, models

class Vendedor(models.Model):
    _name = 'vendedores.reg'
    _description = 'Vendedores registrados'

    name = fields.Char("Nombre del vendedor")
    direccion_vendedor = fields.Text('Dirección del vendedor')
    cedula_vendedor = fields.Char("Cédula del vendedor")

    status = fields.Selection(selection = [('disponible', 'Disponible'), ('no_disponible', 'No disponible')])

    imagen = fields.Binary()