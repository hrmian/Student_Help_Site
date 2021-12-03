from django.contrib import admin
from Application.models import *

# Register your models here.
admin.site.register(User)
admin.site.register(UserProfile)
admin.site.register(Course)
admin.site.register(Thread)
admin.site.register(Post)
admin.site.register(Notification)
admin.site.register(Subscription)
admin.site.register(Report)
