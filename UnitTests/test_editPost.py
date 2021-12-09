from django.test import TestCase
from django.urls import reverse
from Application.models import User, Course, Thread, Notification, Post, Subscription


class TestEditPost(TestCase):
    def setUp(self):
        user = User(username="user1", email="user1@uwm.edu")
        user.set_password("a12345678!")
        user.save()
        self.user = user

        course = Course.objects.create(name="CS595", professor=self.user)
        self.thread = Thread.objects.create(course=course, subject="Project", user=self.user)

        self.post = Post.objects.create(
            content="Project Question",
            user=user,
            thread=self.thread
        )

    def login(self):
        self.client.login(username=self.user.username, password="a12345678!")

    def test_editPost(self):
        self.login()
        Subscription.objects.create(
            user=self.user,
            thread=self.thread
        )
        response = self.client.post(reverse("edit_post", args=[self.post.id]), {
            "content": "Sample Output"
        })

        self.assertEqual(response.status_code, 302)
        self.assertTrue(Notification.objects.all().exists())
        self.assertTrue(Post.objects.get(id=self.post.id).content == "Sample Output")

