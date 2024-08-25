""" Initialize Abstract Customer """
from odoo import fields, models, api, _


class AccountAssetsCategory(models.Model):
    _name = 'account.assets.category'
    _description = 'Assets Category'
    _inherit = ['mail.thread.main.attachment', 'mail.activity.mixin']
    _parent_name = "parent_id"
    _parent_store = True
    _rec_name = 'complete_name'
    _order = 'complete_name'

    name = fields.Char(required=True, tracking=True)
    parent_id = fields.Many2one('account.assets.category', tracking=True)
    complete_name = fields.Char(
        'Complete Name', compute='_compute_complete_name', recursive=True,
        store=True)
    parent_path = fields.Char(index=True, unaccent=False)

    @api.depends('name', 'parent_id.complete_name')
    def _compute_complete_name(self):
        for rec in self:
            if rec.parent_id:
                rec.complete_name = '%s / %s' % (rec.parent_id.complete_name, rec.name)
            else:
                rec.complete_name = rec.name
