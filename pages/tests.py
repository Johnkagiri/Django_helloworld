from django.test import SimpleTestCase, TestCase
from django.urls import reverse
from .models import Post

# Create your tests here.
class HomePageTests(SimpleTestCase):
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_url_available_by_name(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)    
        
class AboutpageTests(SimpleTestCase):
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/about")
        self.assertEqual(response.status_code, 200)

    def test_url_available_by_name(self): 
        response = self.client.get(reverse("about"))
        self.assertEqual(response.status_code, 200)

class PostTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.post=Post.objects.create(text="This is a test")

    def test_model_content(self):
        self.assertEqual(self.post.text, "This is a test")    
                

