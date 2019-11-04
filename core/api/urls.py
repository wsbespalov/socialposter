from django.urls import path

from .views import UserAPIView
from .views import UserDetailAPIView
from .views import InstagramAPIView


urlpatterns = [
    path('user/', UserAPIView.as_view()),
    path('user/<int:pk>/', UserDetailAPIView.as_view()),
    path('instagram/', InstagramAPIView.as_view()),
]