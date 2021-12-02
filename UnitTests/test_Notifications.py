from django.test import TestCase
from django.urls import reverse
from Application.models import User, Course, Thread, Notification


class TestNotifications(TestCase):
    def setUp(self) -> None:
        user = User(username="user1", email="user2@gmail.com")
        user.set_password("12345678")
        user.save()
        self.user = user

        user2 = User(username="user2", email="user2@gmail.com")
        user2.save()
        self.user2 = user2

        course = Course.objects.create(name="sample_course", professor=self.user)
        self.thread_1 = Thread.objects.create(course=course, subject="thread_1", user=self.user)
        self.thread_2 = Thread.objects.create(course=course, subject="thread_2", user=self.user)

        self.notification_1 = Notification.objects.create(
            from_user=user2,
            to_user=self.user,
            thread=self.thread_1,
            notification_type=1,
        )

        self.notification_2 = Notification.objects.create(
            from_user=self.user,
            to_user=user2,
            thread=self.thread_2,
            notification_type=1,
        )

        self.notification_3 = Notification.objects.create(
            from_user=user2,
            to_user=self.user,
            thread=self.thread_2,
            notification_type=1,
        )

        self.notification_4 = Notification.objects.create(
            from_user=user2,
            to_user=self.user,
            thread=self.thread_1,
            notification_type=1,
        )

    def login(self):
        self.client.login(username=self.user.username, password="12345678")

    def test_threadNotification(self):
        self.login()
        response_1 = self.client.get(reverse("thread_notification", args=[
            self.notification_1.id,
            self.thread_1.id
        ]))

        self.assertTrue(response_1.url == reverse("thread", args=[self.notification_1.thread_id]))
        self.assertTrue(Notification.objects.get(id=self.notification_1.id).seen)

        response_2 = self.client.get(reverse("thread_notification", args=[
            self.notification_2.id,
            self.thread_1.id
        ]))

        self.assertEqual(response_2.status_code, 404)
        self.assertFalse(Notification.objects.get(id=self.notification_2.id).seen)

    def test_NotificationHandlesLogin(self):
        url = reverse("thread_notification", args=[
            self.notification_1.id,
            self.thread_1.id
        ])
        response = self.client.get(url)

        self.assertTrue(response.url == f"{reverse('login')}?next={url}")
        self.assertTrue(response.status_code == 302)

    def test_clearNotification(self):
        self.login()
        response = self.client.get(reverse("clear_notification", args=[self.notification_1.id]),
                                   HTTP_REFERER=reverse("home"))

        self.assertTrue(Notification.objects.get(id=self.notification_1.id).seen)
        self.assertFalse(Notification.objects.get(id=self.notification_2.id).seen)
        self.assertFalse(Notification.objects.get(id=self.notification_3.id).seen)
        self.assertFalse(Notification.objects.get(id=self.notification_4.id).seen)

        self.assertTrue(response.url == reverse("home"))
        self.assertTrue(response.status_code == 302)

        response_2 = self.client.get(reverse("clear_notification", args=[self.notification_2.id]))

        self.assertEqual(response_2.status_code, 404)
        self.assertFalse(Notification.objects.get(id=self.notification_2.id).seen)

    def test_ClearNotificationHandlesLogin(self):
        url = reverse("clear_notification", args=[
            self.notification_1.id
        ])
        response = self.client.get(url)

        self.assertTrue(
            response.url == f"{reverse('login')}?next={url}")
        self.assertTrue(response.status_code == 302)

    def test_ClearAllNotifications(self):
        self.login()
        response = self.client.get(reverse("clear_notifications"), HTTP_REFERER=reverse("home"))
        self.assertTrue(response.url == reverse("home"))
        self.assertTrue(response.status_code == 302)

        self.assertEqual(Notification.objects.filter(to_user=self.user, seen=False).count(), 0)
        self.assertEqual(Notification.objects.filter(to_user=self.user2, seen=False).count(), 1)

    def test_ClearAllNotificationsHandlesLogin(self):
        response = self.client.get(reverse("clear_notifications"))

        self.assertTrue(response.url == f"{reverse('login')}?next={reverse('clear_notifications')}")
        self.assertTrue(response.status_code == 302)
