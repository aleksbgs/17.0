# models/test_applicant.py
from odoo import models, fields, api



class TestApplicant(models.Model):
    _name = 'test.applicant'
    _description = 'Test Applicant'

    name = fields.Char(string='Name', required=True)
    description = fields.Text(string='Description')
    active = fields.Boolean(string='Active', default=True)
    reference_code = fields.Char(string='Reference Code', readonly=True, copy=False, compute='_compute_reference_code', store=True)
    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirmed', 'Confirmed'),
        ('done', 'Done')
    ], string='State', default='draft')

    @api.depends('name')
    def _compute_reference_code(self):
        for record in self:
            if not record.reference_code:
                last_record = self.search([], order='id desc', limit=1)
                last_number = int(last_record.reference_code.split('-')[-1]) if last_record.reference_code else 0
                record.reference_code = f'TEST-{last_number + 1:04d}'

    def action_confirm(self):
        self.write({'state': 'confirmed'})