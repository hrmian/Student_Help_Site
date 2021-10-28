from django.contrib import admin
from Application.models import *

# Register your models here.
admin.site.register(User)
admin.site.register(Course)
admin.site.register(Topic)
admin.site.register(Reply)