from odoo import models, fields, api, _
from odoo.exceptions import AccessError

class ResUsers(models.Model):
    _inherit = 'res.users'

    def action_login_as(self):
        self.ensure_one()
        if not self.env.user.has_group('base.group_system'):
            raise AccessError(_('You do not have permission to use this feature.'))
        if self.id == self.env.ref('base.user_root').id:
            raise AccessError(_('Logging in as the superuser is not allowed.'))
        return {
            'type': 'ir.actions.client',
            'tag': 'login_as_user',
            'target': 'new',
            'params': {'user_id': str(self.id) if self.id else ""}
        }
