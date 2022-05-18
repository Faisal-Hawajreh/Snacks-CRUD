from django.test import TestCase
from django.urls import reverse


# Create your tests here.
class SnackTest(TestCase):
    def test_list_page_status_code(self):
        url = reverse("snacks_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    
    def test_list_page_tamplate(self):
        url = reverse("snacks_list")
        response = self.client.get(url)
        self.assertTemplateUsed(response, "snacks_list.html")
        self.assertTemplateUsed(response, "base.html")

    # def test_detail_page_status_code(self):
    #     url = reverse("snack_detail")
    #     response = self.client.get(url)
    #     self.assertEqual(response.status_code, 200)

    
    # def test_detail_page_tamplate(self):
    #     url = reverse("snack_detail")
    #     response = self.client.get(url)
    #     self.assertTemplateUsed(response, 'snack_detail.html')
    #     self.assertTemplateUsed(response, "base.html")
