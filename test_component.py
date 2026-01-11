import unittest
import json
from src.app import app

class TestModelServing(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_predict_endpoint(self):
        response = self.app.post('/predict', 
                                 data=json.dumps({'feature': 'user_123'}),
                                 content_type='application/json')
        data = json.loads(response.get_data(as_text=True))
        
        self.assertEqual(response.status_code, 200)
        self.assertIn('prediction', data)
        self.assertIn('bucket', data)
        self.assertEqual(data['feature'], 'user_123')

    def test_health_endpoint(self):
        response = self.app.get('/health')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.get_data(as_text=True)), {'status': 'healthy'})

if __name__ == '__main__':
    unittest.main()
