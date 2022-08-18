from odoo import models, fields


class SampleStatusWizard(models.TransientModel):
    _name = 'sample.status.wizard'
    _description = 'Set Sample Status'
    _inherit = ['mail.activity.mixin', 'mail.thread']


    status = fields.Selection(selection=[
        ('ready', 'Ready'),
        ('complete', 'Complete')], default='ready', string='Status', tracking=True)


    def update_statuses(self):
        items = self.env['sample_model'].browse(
            self._context.get('active_ids', [])
        )
        for item in items:
            item.update({"status": self.status})