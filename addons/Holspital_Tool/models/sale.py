import base64

from odoo import models, fields, modules, api, _
from odoo.exceptions import ValidationError


def get_default_img(name_image):
        with open(modules.get_module_resource('Holspital_Tool', 'static/description', name_image),
              'rb') as f:
            return base64.b64encode(f.read())

class SaleORder(models.Model):
    _inherit = 'sale.order'


    sale_description = fields.Char(string = "Descripcion de venta")