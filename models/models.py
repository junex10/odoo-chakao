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

    name = fields.Char('Titulo del reporte')

class Presupuestos(models.Model):
    _inherit = "sale.order"

    nombre_vendedor = fields.Many2one('vendedores.reg', 'Vendedor')
    rif = fields.Char("Rif")
    direccion_factura = fields.Char("Dirección de factura")
    direccion_entrega = fields.Char("Dirección de entrega")
    tarifa = fields.Float("Tarifa")
    moneda_referencia = fields.Selection(selection=[('ptr', 'PTR')])
    asignacion = fields.Selection(selection=[('gerente_ventas', 'Gerente de Ventas'), ('gerencia_credito', 'Gerencia de Crédito y Cobranzas')])
    por_aprobar = fields.Selection(selection=[('gerente_ventas', 'Gerente de Ventas'), ('gerencia_credito', 'Gerencia de Crédito y Cobranzas')])

    lapso_reserva_ini = fields.Date(string="Lapso de reserva inicial")
    lapso_reserva_end = fields.Date(string="Lapso de reserva final")

    fecha_estimada = fields.Date(string="Fecha estimada de entrega")
    observaciones = fields.Text()
    aprobacion = fields.Boolean(string="Aprobado", default=False)
    no_aprobado = fields.Boolean(string="Rechazado", default=False)
