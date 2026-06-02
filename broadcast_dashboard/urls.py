# broadcast_dashboard/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path("", views.dashboard_stats, name="dashboard_stats"),

    path("settings/", views.dashboard_settings, name="dashboard_settings"),

    path("csrf/", views.csrf_token, name="csrf_token"),
    path("auth/status/", views.auth_status, name="auth_status"),
    path("auth/login/", views.login_api, name="login_api"),
    path("auth/logout/", views.logout_api, name="logout_api"),
]
