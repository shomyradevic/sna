from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from .models import Profile
from posts.models import Post

"""
Mali signali
"""
User = get_user_model()


@receiver(signal=post_save, sender=User)
def create_profile(instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(signal=post_save, sender=User)
def save_profile(instance, **kwargs):
    instance.profile.save()


@receiver(signal=pre_delete, sender=User)
def delete_uploaded_images(instance, **kwargs):
    user = User.objects.filter(username=instance).get()
    posts = Post.objects.filter(author=user)
    for post in posts:
        if post.image:
            post.image.delete()
