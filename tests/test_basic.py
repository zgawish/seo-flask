import unittest, sys

sys.path.append('../seo-flask') # imports python file from parent directory
from demo import app #imports flask app object

class BasicTests(unittest.TestCase):

    # executed prior to each test
    def setUp(self):
        self.app = app.test_client()

    ###############
    #### tests ####
    ###############

    def test_main_page(self):
        response = self.app.get('/', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
    
    def test_register_page(self):
        response = self.app.get('/register', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
    
    def test_second_page(self):
        response = self.app.get('/second_page', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        
    def test_fake_page(self):
        response = self.app.get('/ding', follow_redirects=True)
        self.assertNotEqual(response.status_code, 200)

if __name__ == "__main__":
    unittest.main()