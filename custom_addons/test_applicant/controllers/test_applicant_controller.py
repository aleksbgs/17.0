import logging
from odoo import http
from odoo.http import request

_logger = logging.getLogger(__name__)


class TestApplicantController(http.Controller):
    @http.route('/api/test-model', auth='public', type='json', methods=['GET'], csrf=False)
    def get_test_applicants(self):
        records = request.env['test.applicant'].search([])
        return [{'id': rec.id, 'name': rec.name, 'reference_code': rec.reference_code, 'state': rec.state} for rec
                in records]

    @http.route('/api/test-model', type='json', auth='user', methods=['POST'], csrf=False)
    def create_test_applicant(self):

        data = request.httprequest.get_json()
        _logger.info("Received data: %s", data)

        api_key = request.httprequest.headers.get('api-key')
        auth_api = auth_api_key(api_key)

        if auth_api:
            if not data or 'name' not in data:
                return {'error': 'Name is required', 'status': 400}

            record = request.env['test.applicant'].sudo().create({
                'name': data['name'],
                'description': data.get('description', ''),
            })

            return {
                'id': record.id,
                'name': record.name
            }
        else:
            return "you are not authorized"


def auth_api_key(api_key):
    user_id = request.env['res.users'].sudo().search([('api_key', '=', api_key)])
    if api_key is not None and user_id:
        response = True
    else:
        response = False
    return response
