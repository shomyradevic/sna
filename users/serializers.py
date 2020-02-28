from .models import CustomUser, Profile
from rest_framework.serializers import HyperlinkedModelSerializer, HyperlinkedRelatedField


class CustomUserSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'url', 'username', 'date_joined', 'profile')


class ProfileSerializer(HyperlinkedModelSerializer):
    user = HyperlinkedRelatedField(view_name='user-detail', read_only=True)

    class Meta:
        model = Profile
        fields = ('image', 'user')
