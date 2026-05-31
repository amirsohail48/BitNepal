from django.urls import path, include, register_converter
from rest_framework.routers import DefaultRouter
from .views import TblpatientdateViewSet
from . import views

router = DefaultRouter()
router.register(r'Tblpatientdate',TblpatientdateViewSet, basename='Tblpatientdate')
    
urlpatterns = [
    path('login/',views.user_login,name='login'),
    path('',views.dashboard,name='dashboard'),
    path('report/a/',views.diagnostic_view, name='diagnostic_view'),
    path('report/',views.report,name='dashboard_report'),
    path('bill/',views.user_login,name='billing_report'),
    path('api/', include(router.urls)),
    path('dashboard/', views.dashboard_stats_api,name='dashboard_api'),
]