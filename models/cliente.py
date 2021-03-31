from odoo import fields, models, api

class Clientes(models.Model):
    _inherit = "res.partner"

    tipo_cliente = fields.Char("Tipo de cliente")
    distribuidor = fields.Boolean(string='Distribuidor',default=False)
    flota = fields.Boolean(string='Flota', default=False)

    consumidor_final = fields.Boolean(string='Consumidor final', default=False)
    otros_entes = fields.Boolean(string='Otros entes', default=False)
    vendedor_asignado = fields.Many2one('vendedores.reg', 'Vendedor')
    zona = fields.Text('Zona')
    condicion_pago = fields.Text('Condición de pago')

class ContactoCliente(models.Model):
    _inherit = 'res.partner'

    horario_entrega = fields.Char("Horario de entrega")
    direccion_entrega_mapa = fields.Binary("Mapa de dirección")