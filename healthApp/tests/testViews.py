from rest_framework.test import APITestCase,APIRequestFactory
from healthApp.views import DonorAPIView
from django.urls import reverse
from rest_framework import status

class TestCase(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.view = DonorAPIView.as_view()
        self.url = reverse("donor_list")

    def test_list_donor(self):
        request = self.factory.get(self.url)

        response = self.view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    def test_create_donor(self):
        pass