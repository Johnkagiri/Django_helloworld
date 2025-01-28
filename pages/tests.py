from django.test import SimpleTestCase, TestCase
from django.urls import reverse
from .models import Post
from django.contrib.auth import get_user_model

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

# class PostTests(TestCase):
#     @classmethod
#     def setUpTestData(cls):
#         cls.post=Post.objects.create(text="This is a test")

#     def test_model_content(self):
#         self.assertEqual(self.post.text, "This is a test")    
                
class BlogTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(username= "testuser", email="test@email.com", password="secret" )
        cls.post = Post.objects.create(title="A good title", body="Nice body content", author=cls.user, ) 
    
    def test_post_model(self):
        self.assertEqual(self.post.title, "A good title")
        self.assertEqual(self.post.body, "Nice body content")
        self.assertEqual( self.post.author.username, "testuser" )
        self.assertEqual( str(self.post), "A good title" )
        self.assertEqual( self.post.get_absolute_url(), "/post/1/" )
    
    def test_url_exists_at_correct_location_listview(self): # new
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
    def test_url_exists_at_correct_location_detailview(self): # new
        response = self.client.get("/post/1/")
        self.assertEqual(response.status_code, 200)
    def test_post_listview(self): # new
        response = self.client.get(reverse("posthome"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Nice body content")
        self.assertTemplateUsed(response, "posthome.html")
    def test_post_detailview(self): # new
        response = self.client.get(reverse("post_detail",
        kwargs={"pk": self.post.pk}))
        no_response = self.client.get("/post/100000/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, "A good title")
        self.assertTemplateUsed(response, "post_detail.html")
    def test_post_createview(self):
        response = self.client.post( reverse("post_new"), {
            "title": "New title",
            "body": "New text",
            "author": self.user.id,
        }, )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Post.objects.last().title,"New title")
        self.assertEqual(Post.objects.last().body, "New text")
    def test_post_updateview(self):
        response = self.client.post(
            reverse("post_edit", args="1"),
            {
                "title":"Updated title",
                "body":"Updated text",
            },
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Post.objects.last().title, "Updated title")
        self.assertEqual(Post.objects.last().body, "Updated text")
    def test_post_deleteview(self):
        response = self.client.post(reverse("post_delete", args="1"))
        self.assertEqual(response.status_code, 302)




