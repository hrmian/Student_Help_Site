from Application.models import Subscription, Notification, Report


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
        if from_user != s.user:
            Notification.objects.create(to_user=s.user, from_user=from_user, thread=thread, notification_type=1)


# submit a report on a post for possible cheating
def report_post(reportedPost, userReporting, userReported):
    if not Report.objects.filter(reportedPost=reportedPost, open=True).exists():
        Report.objects.create(userReporting=userReporting, userReported=userReported, reportedPost=reportedPost)
        thread = reportedPost.thread
        professor = thread.course.professor
        Notification.objects.create(to_user=professor, from_user=userReporting, thread=thread, notification_type=3)


def get_reports(request):
    user = request.user
    if user.role == 'Admin':
        return Report.objects.filter(open=True)
    elif user.role == 'Professor':
        return Report.objects.filter(reportedPost__thread__course__professor=user, open=True)
