# -*- coding: utf-8 -*-

from odoo import models, fields, api

# class export_order_dimabe(models.Model):
#     _name = 'export_order_dimabe.export_order_dimabe'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100