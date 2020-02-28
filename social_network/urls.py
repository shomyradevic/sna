"""social_network URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf.urls.static import static
from social_network import settings
from users.views import (
    register_view,
    login_view,
    logout_view,
    profile_update_view,
    ProfileDetailView,
    AccountDeleteView,
)
from rest_framework.routers import DefaultRouter
from posts.views import PostViewSet
from users.views import CustomUserViewSet, ProfileViewSet

router = DefaultRouter()
router.register('users', CustomUserViewSet)
router.register('posts', PostViewSet)
router.register('profiles', ProfileViewSet)

user_detail = CustomUserViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

urlpatterns = [
    path('', include('posts.urls')),
    path('profile/<int:pk>/update', profile_update_view, name='profile-update'),
    path('profile/<int:pk>/delete', AccountDeleteView.as_view(template_name='users/delete_profile.html'), name='profile-delete'),
    path('profile/<int:pk>/', ProfileDetailView.as_view(), name='profile-detail'),
    path('api/', include(router.urls)),
    path('api/users/<int:pk>/', user_detail, name='user-detail'),
    path('logout/', logout_view, name='logout'),
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('admin/', admin.site.urls)
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
