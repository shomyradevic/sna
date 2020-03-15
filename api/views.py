from rest_framework import generics, mixins
from posts.models import Post
from users.models import CustomUser, Profile
from .serializers import PostSerializer, CustomUserSerializer, RegistrationSerializer, ProfileSerializer
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .permissions import IsAdminOrOwner
from rest_framework.views import APIView

custom_perm = IsAdminOrOwner()


class ProfileListView(generics.ListAPIView):
    serializer_class = ProfileSerializer
    permission_classes = (permissions.AllowAny, )

    def get_queryset(self):
        return Profile.objects.all()


class ProfileRUDView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProfileSerializer
    permission_classes = (permissions.AllowAny, )
    permission_error_message = custom_perm.generate_error_message('profile')

    def put(self, request, *args, **kwargs):
        if custom_perm.has_object_permission(request=request, obj=self.get_object().user):
            return self.update(request=request, args=args, kwargs=kwargs)
        return Response(data=self.permission_error_message, status=status.HTTP_403_FORBIDDEN)

    def patch(self, request, *args, **kwargs):
        if custom_perm.has_object_permission(request=request, obj=self.get_object().user):
            return self.partial_update(request=request, args=args, kwargs=kwargs)
        return Response(data=self.permission_error_message, status=status.HTTP_403_FORBIDDEN)

    def delete(self, request, *args, **kwargs):
        pass

    def get_queryset(self):
        return Profile.objects.all()


@api_view(['POST', ])
def rest_register(request):
    if request.method == 'POST':
        user = RegistrationSerializer(data=request.data)
        if user.is_valid():
            data = {}
            new_user = user.save()
            data['username'] = new_user.username
            data['email'] = new_user.email
            data['url'] = new_user.get_api_url(request=request)
        else:
            data = user.errors
        return Response(data=data, status=status.HTTP_201_CREATED)


class PostLCView(mixins.CreateModelMixin, generics.ListAPIView):
    serializer_class = PostSerializer
    permission_classes = (permissions.AllowAny, )

    # We must override this because we have to make a
    # is_authenticated condition before saving post instance.
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_queryset(self):
        return Post.objects.all()

    def post(self, request, *args, **kwargs):
        error_response = {'message': 'Only authenticated user can create a post.'}
        if self.request.user.is_authenticated:
            return self.create(request=request, args=args, kwargs=kwargs)
        return Response(data=error_response, status=status.HTTP_401_UNAUTHORIZED)


class PostRUDView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PostSerializer
    permission_classes = (permissions.AllowAny, )
    permission_error_message = custom_perm.generate_error_message('post')

    def validate_content_and_image(self) -> dict:
        response = {'flag': False}
        if 'image' not in self.request.data and 'content' not in self.request.data:
            response['error'] = {'message': 'Post must contain either image or text.'}
            return response

        elif self.get_object().image:
            if 'image' in self.request.data.keys():
                response['flag'] = True
            elif 'content' in self.request.data.keys():
                response['error'] = {'message': 'You can not text-edit an image post.'}

        elif self.get_object().content:
            if 'image' in self.request.data.keys():
                response['error'] = {'message': 'You can not upload image on text-post.'}
            elif 'content' in self.request.data.keys():
                if len(self.request.data['content']) > 2:
                    response['flag'] = True
                else:
                    response['error'] = {'message': 'Content must be at least 3 characters long.'}
        return response

    def put(self, request, *args, **kwargs):
        if custom_perm.has_object_permission(request=request, obj=self.get_object().author):
            report = self.validate_content_and_image()
            if report['flag']:
                return self.update(request=request, args=args, kwargs=kwargs)
            else:
                return Response(
                    data=report['error'],
                    status=status.HTTP_406_NOT_ACCEPTABLE
                )
        return Response(data=self.permission_error_message, status=status.HTTP_403_FORBIDDEN)

    def patch(self, request, *args, **kwargs):
        if custom_perm.has_object_permission(request=request, obj=self.get_object().author):
            report = self.validate_content_and_image()
            if report['flag']:
                return self.partial_update(request=request, args=args, kwargs=kwargs)
            else:
                return Response(
                    data=report['error'],
                    status=status.HTTP_406_NOT_ACCEPTABLE
                )
        return Response(data=self.permission_error_message, status=status.HTTP_403_FORBIDDEN)

    def delete(self, request, *args, **kwargs):
        if custom_perm.has_object_permission(request=request, obj=self.get_object().author):
            return self.destroy(request=request, args=args, kwargs=kwargs)
        return Response(data=self.permission_error_message, status=status.HTTP_403_FORBIDDEN)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance=instance)
        return Response(data={'message': 'Post successfully deleted.'}, status=status.HTTP_200_OK)

    def get_queryset(self):
        return Post.objects.all()


class UserRUDView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CustomUserSerializer
    permission_classes = (permissions.AllowAny, )
    permission_error_message = custom_perm.generate_error_message('user')

    def put(self, request, *args, **kwargs):
        if custom_perm.has_object_permission(request=request, obj=self.get_object()):
            return self.update(request=request, args=args, kwargs=kwargs)
        return Response(data=self.permission_error_message, status=status.HTTP_403_FORBIDDEN)

    def patch(self, request, *args, **kwargs):
        if custom_perm.has_object_permission(request=request, obj=self.get_object()):
            return self.partial_update(request=request, args=args, kwargs=kwargs)
        return Response(data=self.permission_error_message, status=status.HTTP_403_FORBIDDEN)

    def delete(self, request, *args, **kwargs):
        if custom_perm.has_object_permission(request=request, obj=self.get_object()):
            return self.destroy(request=request, args=args, kwargs=kwargs)
        return Response(data=self.permission_error_message, status=status.HTTP_403_FORBIDDEN)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance=instance)
        return Response(data={'message': 'Post successfully deleted.'}, status=status.HTTP_200_OK)

    def get_queryset(self):
        return CustomUser.objects.all()


class UserListView(generics.ListAPIView):
    serializer_class = CustomUserSerializer
    permission_classes = (permissions.AllowAny, )

    def get_queryset(self):
        return CustomUser.objects.all()


class DocsView(APIView):

    def get(self, request, *args, **kwargs):
        apidocs = {
            'register': request.build_absolute_uri('register/'),
            'login': request.build_absolute_uri('token/'),
            'token-refresh': request.build_absolute_uri('token/refresh'),
            'posts': request.build_absolute_uri('posts/'),
            'users': request.build_absolute_uri('users/'),
            'profiles': request.build_absolute_uri('profiles/')
        }
        return Response(data=apidocs)