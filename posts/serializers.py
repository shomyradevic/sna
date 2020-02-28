from .models import Post
from rest_framework.serializers import HyperlinkedModelSerializer


class PostSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'url', 'author', 'created_time', 'content', 'image')
