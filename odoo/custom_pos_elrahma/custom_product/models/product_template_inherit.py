# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, tools, _, SUPERUSER_ID




class ProductTemplate(models.Model):
    _inherit = "product.template"

    #
    # @api.onchange('list_price','tax_string')
    # def _onchange_list_price(self):
    #     if self.list_price and self.tax_string:
    #         self.list_price = self.list_price + self.taxes_id.amount
    #         self.tax_string=self._construct_tax_string(self.list_price + self.taxes_id.amount)

    #
    # @api.depends('taxes_id', 'list_price')
    # def _compute_tax_string(self):
    #     for record in self:
    #         record.tax_string = record._construct_tax_string(record.list_price + record.taxes_id.amount)