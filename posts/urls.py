from django.urls import path
import posts.views as postviews


urlpatterns = [
    path('', postviews.home, name='homepage'),
    path('image/', postviews.image, name='image-create'),
    path('post/<int:pk>/', postviews.PostDetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/edit/', postviews.post_edit_view, name='post-edit'),
    path('post/<int:pk>/delete/', postviews.delete_view, name='post-delete'),
    path('user/<str:username>/posts/', postviews.UserPostsView.as_view(), name='user-posts'),
    path('like/', postviews.like, name='like')
]
