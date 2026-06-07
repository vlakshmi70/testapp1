from django.test import TestCase
from django.http import HttpRequest
from lists.views import home_page

# Create your tests here.

class SmokeTest(TestCase):
    def test_bad_maths(self):
        self.assertEqual(1+1,2)

class HomePageTest(TestCase):
    def test_home_page_template(self):
        resp = self.client.get("/")
        self.assertTemplateUsed(resp, "home.html")

    def test_home_page_content(self):
        resp = self.client.get("/")
        self.assertContains(resp, "To-Do")
