from django.test import TestCase
from django.urls import reverse
from Application.models import User, Course, Thread, Notification, Post


class TestHidePost(TestCase):
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

    def test_hidePost(self):
        self.login()
        response = self.client.get(reverse("hide_post", args=[self.thread.id, self.post.id, 0]))

        self.assertEqual(response.status_code, 302)
        self.assertFalse(Post.objects.get(id=self.post.id).visible)
        self.assertTrue(
            Notification.objects.filter(to_user=self.post.user, from_user=self.user, thread=self.post.thread,
                                        notification_type=2).exists())

    def test_visiblePost(self):
        self.login()
        response = self.client.get(reverse("hide_post", args=[self.thread.id, self.post.id, 1]))
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Post.objects.get(id=self.post.id).visible)
        self.assertTrue(
            Notification.objects.filter(to_user=self.post.user, from_user=self.user, thread=self.post.thread,
                                        notification_type=2).count() == 0)
