from django.db import models
from PIL import Image
from django.shortcuts import reverse
from django.contrib.auth import get_user_model


class Post(models.Model):
    author = models.ForeignKey(to=get_user_model(), on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True)
    content = models.TextField(blank=True)
    image = models.ImageField(upload_to='uploaded', blank=True, null=True)
    likes = models.ManyToManyField(to=get_user_model(), blank=True, related_name='post_likes')

    def get_absolute_url(self):
        return reverse(viewname='homepage')

    def resize_proportionally_and_save(self, image, w_or_h=None):
        if w_or_h == 'w': # if width if greater than height
            image.thumbnail((600, image.height * 600 / image.width))
        elif w_or_h == 'h': # if height if greater than width
            image.thumbnail((image.height * 600 / image.width, 600))
        else: # if height and width are equal
            image.thumbnail((600, 600))
        image.save(self.image.path)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        super().save()
        if self.image:
            image = Image.open(self.image.path)
            if image.width > 600 or image.height > 600:
                if image.width - image.height > 0:
                    self.resize_proportionally_and_save(w_or_h='w', image=image)
                elif image.height - image.width > 0:
                    self.resize_proportionally_and_save(w_or_h='h', image=image)
                elif image.height == image.width:
                    self.resize_proportionally_and_save(image=image)

    def set_likes_and_save(self, likes):
        self.likes = likes
        self.save()

    def set_text_and_save(self, text_content):
        self.content = text_content
        self.save()

    def set_image_and_save(self, image):
        self.image = image
        self.save()

    def __str__(self):
        return self.author.username + "'s post"
