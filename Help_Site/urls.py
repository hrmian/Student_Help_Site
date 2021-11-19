"""Help_Site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from Application import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/sign_up', views.sign_up, name="sign_up"),
    path('accounts/forgot_password', views.forgot_password, name="forgot_password"),
    path('profile/<slug:username>', views.user_profile, name="profile"),
    path('settings/<slug:username>', views.settings, name="settings"),
    path('settings/accountsettings/<slug:username>', views.user_settings, name="user_settings"),
    path('settings/adminusersettings/<slug:username>', views.admin_user_settings, name="admin_user_settings"),
    path('discussions/<int:course_id>', views.discussions, name="discussions"),
    path('discussions/<int:course_id>/newthread', views.create_thread, name="create_thread"),
    path('thread/<int:thread_id>/', views.thread, name="thread"),
    path('notification/<int:notification_id>/thread/<int:thread_id>', views.thread_notification,
         name='thread_notification'),
    path('notifications/clear_all', views.clear_all_notifications, name="clear_notifications"),
    path('notifications/clear/<int:notification_id>', views.clear_notification, name='clear_notification'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
