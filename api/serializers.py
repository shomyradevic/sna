from rest_framework import serializers
from posts.models import Post
from users.models import CustomUser, Profile
from api.help import log


class RegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(min_length=8, style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password', 'password2')

    def save(self, **kwargs):
        user = CustomUser(username=self.validated_data['username'], email=self.validated_data['email'])
        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        if password != password2:
            raise serializers.ValidationError({'password': 'Passwords do not match.'})
        user.set_password(password)
        user.save()
        return user


class PostSerializer(serializers.ModelSerializer):
    post_url = serializers.SerializerMethodField(read_only=True)
    author = serializers.SerializerMethodField(read_only=True)
    likes = serializers.SerializerMethodField(read_only=True)

    read_only_fields = ('post_url', 'author', 'created_time', 'likes')

    class Meta:
        model = Post
        fields = ('post_url', 'author', 'created_time', 'content', 'image', 'likes')

    """def save(self, **kwargs):
        image, content = '', ''
        if 'image' in self.validated_data.keys():
            image = self.validated_data['image']
        if 'content' in self.validated_data.keys():
            content = self.validated_data['content']
        
        # We must handle case when user uploads both image and content.
        # What takes priority? Image like on website?
        #user.save()
        #return user"""


    def get_post_url(self, obj):
        request = self.context.get('request')
        return obj.get_api_url(request=request)

    def get_author(self, obj):
        request = self.context.get('request')
        return obj.author.get_api_url(request=request)

    def get_likes(self, obj):
        request = self.context.get('request')
        likes = [user.get_api_url(request=request) for user in obj.likes.all()]
        return likes


class CustomUserSerializer(serializers.ModelSerializer):
    user_url = serializers.SerializerMethodField(read_only=True)
    is_staff = serializers.SerializerMethodField(read_only=True)

    read_only_fields = ('user_url', 'username', 'first_name', 'last_name', 'email', 'is_staff', 'date_joined')
    class Meta:
        model = CustomUser
        fields = ('user_url', 'username', 'first_name', 'last_name', 'email', 'date_joined', 'is_staff')

    def get_user_url(self, obj):
        request = self.context.get('request')
        return obj.get_api_url(request=request)

    def get_is_staff(self, obj):
        return obj.is_staff