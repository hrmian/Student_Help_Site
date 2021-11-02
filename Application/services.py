from Application.models import Subscription, Notification


def subscribe(user, thread):
    if not Subscription.objects.filter(user=user, thread=thread).exists():
        Subscription.objects.create(user=user, thread=thread)


def send_notifications(from_user, thread):
    subscriptions = Subscription.objects.filter(thread=thread)
    for s in subscriptions:
        Notification.objects.create(to_user=s.user, from_user=from_user, thread=thread, notification_type=1)