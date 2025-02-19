from odoo.tests import HttpCase, tagged
from odoo.addons.test_applicant.controllers import test_applicant_controller

@tagged('post_install', '-at_install')
class TestApplicantControllerTest(HttpCase):

    def test_get_test_applicants(self):
        # Simulate a GET request to the controller
        response = self.url_open('/api/test-model')
        self.assertEqual(response.status_code, 200)
        # Further assertions based on your controller's response

    def test_create_test_applicant(self):
        # Simulate a POST request to the controller
        payload = {
            'jsonrpc': '2.0',
            'params': {
                'name': 'Jane Doe',
                'description': 'New applicant'
            }
        }
        response = self.url_open(
            '/api/test-model',
            data=json.dumps(payload),
            headers={'Content-Type': 'application/json'}
        )
        self.assertEqual(response.status_code, 200)
        # Further assertions based on your controller's response
