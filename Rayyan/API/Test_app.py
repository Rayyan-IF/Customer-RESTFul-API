from flask import Flask
import unittest
from flask_testing import TestCase

from app import app

class TestApp(TestCase):
    
    def create_app(self):
        app.config['Testing'] = True
        return app
    # Get Customer Test
    def test_index(self):
        response = self.client.get('/customer')
        self.assert200(response)
    # Post Customer Test
    def test_register(self):
        response = self.client.post('/customer', 
            json={"created_at": "2020-08-01T10:56:31", "email": "adrien.philippe@gmail.com","gender": "M","image": "https://img.freepik.com/premium-vector/man-avatar-profile-round-icon_24640-14044.jpg",
          "name": "Adrien Philippe Ramos 9", "phone_number": "085222334445", "title": "Ms", 
          "updated_at": "2020-08-08T09:30:23"
            })
        self.assert200(response)

if __name__ == '__main__':
    unittest.main()