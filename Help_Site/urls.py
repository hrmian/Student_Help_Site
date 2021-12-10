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
    path('', views.home, name="home"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/sign_up', views.sign_up, name="sign_up"),
    path('accounts/forgot_password', views.forgot_password, name="forgot_password"),

    path('admin/', admin.site.urls),

    path('discussions/<int:course_id>', views.discussions, name="discussions"),
    path('discussions/<int:course_id>/newthread', views.create_thread, name="create_thread"),
    path('discussions/newcourse', views.create_course, name="create_course"),

    path('edit/<int:post_id>', views.edit_post, name="edit_post"),

    path('messages/<slug:username>', views.messages, name="messages"),
    path('messages/conversation/<int:conversation_id>', views.conversation, name="conversation"),
    path('messages/new_conversation/<slug:username>', views.new_conversation, name="new_conversation"),

    path('notification/<int:notification_id>/thread/<int:thread_id>', views.thread_notification,
         name='thread_notification'),
    path('notification/<int:notification_id>/', views.report_notification,
         name='report_notification'),
    path('notifications/clear_all', views.clear_all_notifications, name="clear_notifications"),
    path('notifications/clear/<int:notification_id>', views.clear_notification, name='clear_notification'),

    path('profile/<slug:username>', views.user_profile, name="profile"),

    path('reports', views.reports_page, name='all_reports'),
    path('reported/<int:post_id>/', views.reported, name="reported"),
    path('report_closed/<int:report_id>/<int:verdict>', views.report_closed, name='report_closed'),

    path('settings/<slug:username>', views.settings, name="settings"),
    path('settings/accountsettings/<slug:username>', views.user_settings, name="user_settings"),
    path('settings/adminusersettings/<slug:username>', views.admin_user_settings, name="admin_user_settings"),

    path('thread/<int:thread_id>/', views.thread, name="thread"),
    path('thread/<int:thread_id>/subscribe', views.thread_subscribe, name="thread_subscribe"),
    path('thread/<int:thread_id>/flag/<int:post_id>/<int:state>', views.hide_post, name="hide_post"),
    path('thread_search/', views.thread_search, name="thread_search_results"),
]
