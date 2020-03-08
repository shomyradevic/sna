from django.urls import path
from .views import PostLCView, PostRUDView, UserRUDView, UserListView, rest_register
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
    path('register/', rest_register, name='api-register'),
    path('token/', TokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),
    path('posts/', PostLCView.as_view(), name='post-list-create'),
    path('posts/<int:pk>/', PostRUDView.as_view(), name='post-rud'),
    path('users/', UserListView.as_view(), name='user-list'),
    path('users/<int:pk>/', UserRUDView.as_view(), name='user-rud')
]