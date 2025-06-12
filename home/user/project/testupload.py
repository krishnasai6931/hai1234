import unittest
import os
from app import app

class TestFileUpload(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_upload_file(self):
        with open('testt.txt', 'rb') as test_file:
            response = self.app.post('/', 
                                     content_type='multipart/form-data',
                                     data={'file': (test_file, 'testt.txt')})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'File testt.txt uploaded successfully', response.data)

    def tearDown(self):
        # Clean up uploaded files after test
        uploads_dir = app.config['UPLOAD_FOLDER']
        for file in os.listdir(uploads_dir):
            os.remove(os.path.join(uploads_dir, file))

if __name__ == '__main__':
    unittest.main()