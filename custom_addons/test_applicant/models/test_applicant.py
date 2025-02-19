from odoo import models, fields, api
from datetime import datetime, timedelta



class TestApplicant(models.Model):
    _name = 'test.applicant'
    _description = 'Test Applicant'

    name = fields.Char(string='Name', required=True)
    description = fields.Text(string='Description')
    active = fields.Boolean(string='Active', default=True)
    reference_code = fields.Char(string='Reference Code', readonly=True, copy=False,
                                 compute='_compute_reference_code', store=True)
    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirmed', 'Confirmed'),
        ('done', 'Done')
    ], string='State', default='draft')
    confirmed_at = fields.Datetime(string='Confirmed At', readonly=True)

    @api.depends('name')
    def _compute_reference_code(self):
        for record in self:
            today_str = fields.Date.today().strftime('%Y-%m-%d')
            last_record = self.search([('create_date', '>=', today_str)], order='id desc', limit=1)
            last_number = int(last_record.reference_code.split('-')[-1]) if last_record.reference_code else 0
            record.reference_code = f'TEST-{last_number + 1:04d}'

    def action_confirm(self):
        self.write({'state': 'confirmed', 'confirmed_at': fields.Datetime.now()})

    @api.model
    def cron_mark_done(self):
        time_threshold = datetime.now() - timedelta(minutes=30)
        records = self.search([('state', '=', 'confirmed'), ('confirmed_at', '<=', time_threshold)])
        records.write({'state': 'done'})

