from django.test import TestCase
from django.urls import reverse
from Application.models import User, Course, Thread, Post


class TestCreateDiscussion(TestCase):
    def setUp(self):
        user = User(username="user1", email="user1@gmail.com")
        user.set_password("12345678")
        user.save()
        self.course = Course.objects.create(name="course_test_1", professor=user)
        self.course_2 = Course.objects.create(name="course_test_2", professor=user)
        self.user = user

    def login(self):
        self.client.login(username=self.user.username, password="12345678")

    def test_validData(self):
        self.login()
        self.client.post(reverse("create_thread", args=[self.course.id]), {
            "subject": "thread test"
        })
        self.client.post(reverse("create_thread", args=[self.course.id]), {
            "subject": "thread test 2"
        })

        self.client.post(reverse("create_thread", args=[self.course_2.id]), {
            "subject": "thread test 3"
        })

        self.assertEqual(Thread.objects.filter(course=self.course).count(), 2)
        self.assertEqual(Thread.objects.filter(course=self.course_2).count(), 1)

    def test_checkTitle(self):
        self.login()
        self.client.post(reverse("create_thread", args=[self.course.id]), {
            "subject": "thread 1",
            "content": "thread 1 content"
        })

        self.client.post(reverse("create_thread", args=[self.course.id]), {
            "subject": "thread 2",
            "content": "thread 2 content"
        })

        self.assertTrue(Thread.objects.filter(subject="thread 1").exists())
        self.assertTrue(Thread.objects.filter(subject="thread 2").exists())


