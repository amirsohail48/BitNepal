from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.dashboard_stats, name="dashboard_stats"),

    path("settings/", views.dashboard_settings, name="dashboard_settings"),

    path("csrf/", views.csrf_token, name="csrf_token"),
    path("auth/status/", views.auth_status, name="auth_status"),
    path("auth/login/", views.login_api, name="login_api"),
    path("auth/logout/", views.logout_api, name="logout_api"),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)