from odoo import models, fields


class SampleModel(models.Model):
    _inherit = ['mail.activity.mixin', 'mail.thread']
    _name = 'sample_model'
    _description = 'Sample Model'

    name = fields.Char(string="Name", tracking=True)
    status = fields.Selection(selection=[
        ('ready', 'Ready'),
        ('complete', 'Complete')], default='ready', string='Status', tracking=True)

    def update_names(self):

        items = self.env['sample_model'].browse(
            self._context.get('active_ids', [])
        )

        for item in items:
            item.update({"name": "updated"})
