from django.urls import path, include
from .views import (
    PostLCView,
    PostRUDView,
    UserRUDView,
    UserListView,
    rest_register,
    ProfileRUDView,
    ProfileListView,
    DocsView
)
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
    path('register/', rest_register, name='api-register'),
    path('token/', TokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),
    path('posts/', PostLCView.as_view(), name='post-list-create'),
    path('posts/<int:pk>/', PostRUDView.as_view(), name='post-rud'),
    path('users/', UserListView.as_view(), name='user-list'),
    path('users/<int:pk>/', UserRUDView.as_view(), name='user-rud'),
    path('profiles/', ProfileListView.as_view(), name='profile-list'),
    path('profiles/<int:pk>/', ProfileRUDView.as_view(), name='profile-rud'),
    path('', DocsView.as_view(), name='docs')
]
