from Application.models import Subscription, Notification


# subscribe a user to a thread
def subscribe(user, thread):
    if not Subscription.objects.filter(user=user, thread=thread).exists():
        Subscription.objects.create(user=user, thread=thread)


def check_subscription(user, thread):
    if Subscription.objects.filter(user=user, thread=thread).exists():
        return True
    else:
        return False


# send out a notification to all users subscribed to a thread
def send_thread_notifications(from_user, thread):
    subscriptions = Subscription.objects.filter(thread=thread)
    for s in subscriptions:
        # from_user != s.user:
        Notification.objects.create(to_user=s.user, from_user=from_user, thread=thread, notification_type=1)