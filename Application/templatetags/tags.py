from django import template
from Application.models import Notification

register = template.Library()


@register.inclusion_tag('display_notifications.html', takes_context=True)
def display_notifications(context):
    user = context['request'].user
    notifications = Notification.objects.filter(to_user=user).exclude(seen=True)
    return {'notifications': notifications}