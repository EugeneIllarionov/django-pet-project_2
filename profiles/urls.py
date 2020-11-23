from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import ProfileDetail


urlpatterns = [
    path('api/profile/<int:pk>', ProfileDetail.as_view(), name='api-profile'),
    ]
