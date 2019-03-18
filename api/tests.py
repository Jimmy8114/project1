from django.test import TestCase
from rest_framework.test import APITestCase
# Create your tests here.

class EntryTests(APITestCase):
    def post_entry(request,self):
        print(request)
        url = "http://127.0.0.1:8000/api/getlist/"
        data = {
            'humanName': request.POST.get('humanName'),
            'humanAge': request.POST.get('humanAge'),
        }
        response = self.client.post(url, data, format='json')
        return response