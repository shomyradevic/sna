from django.shortcuts import render, redirect
from .models import Post
from django.http import JsonResponse
from .forms import PostImageForm, PostTextForm
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView
from django.contrib.messages import warning, success
from django.db.models import Q
from django.core.paginator import Paginator
from django.contrib.auth import get_user_model
from os import remove
from rest_framework.viewsets import ModelViewSet


class PostDetailView(DetailView):
    model = Post


class UserPostsView(ListView):
    model = Post
    paginate_by = 10
    context_object_name = 'posts'

    def get_queryset(self):
        user = get_user_model().objects.filter(username=self.kwargs['username']).get()
        return Post.objects.filter(author=user).order_by('-created_time')


@login_required
def post_edit_view(request, pk: int):
    post = Post.objects.filter(pk=pk).get()
    if request.user == post.author:
        if post.image:
            if request.method == 'POST':
                form = PostImageForm(request.POST, files=request.FILES)
                if 'image' in request.FILES.keys():
                    image_to_delete = post.image
                    post.set_image_and_save(image=request.FILES['image'])
                    remove(image_to_delete.path)
                    success(request=request, message='Post successfully updated.')
                    return redirect(to='homepage')
                else:
                    warning(request=request, message='You must choose a image!')
            else:
                form = PostImageForm(initial={'image': post.image})
        elif post.content:
            if request.method == 'POST':
                form = PostTextForm(request.POST)
                text_content = request.POST.get('content')
                if len(text_content) > 2:
                    post.set_text_and_save(text_content=text_content)
                    success(request=request, message='Post successfully updated.')
                    return redirect(to='homepage')
                else:
                    warning(request=request, message='Text post must be at least 3 characters long.')
            else:
                form = PostTextForm(initial={'content': post.content})
        return render(request=request, template_name='posts/post_update.html', context={'form': form})
    else:
        warning(request=request, message="You cannot edit somebody's post!")
        return redirect(to='homepage')


def home(request):
    if request.is_ajax():
        response = {'status': ''}
        content = request.POST.get('text')
        if content:
            Post(content=content, author=request.user).save()
            response['status'] = 'Post saved'
        else:
            query = request.GET.get('q')
            if query:
                filtered_post_contents = []
                fetched = Post.objects.filter(Q(content__icontains=query))
                for f in fetched:
                    display = f.content[:70] + '...'
                    filtered_post_contents.append(dict({'content': display, 'pk': f.pk}))
                    if len(filtered_post_contents) == 5:
                        break
                response['status'] = filtered_post_contents
        return JsonResponse(data=response)
    else:
        # request.method is GET
        posts = Post.objects.all().order_by('-created_time')
        paginator = Paginator(object_list=posts, per_page=10)
        page = request.GET.get('page')
        posts = paginator.get_page(page)
        return render(request=request, template_name='posts/homepage.html', context={'posts': posts})


@login_required
def image(request):
    if request.method == 'POST':
        image_form = PostImageForm(request.POST, files=request.FILES)
        if 'image' in request.FILES:
            instance = image_form.save(commit=False)
            instance.author = request.user
            instance.save()
            success(request=request, message='Post created successfully')
            return redirect(to='homepage')
        warning(request=request, message='You must pick a image first!')
    else:
        image_form = PostImageForm()
    return render(request=request, template_name='posts/image.html', context={'image_form': image_form})


@login_required
def delete_view(request, pk: int):
    response = {'status': ''}
    post_to_delete = Post.objects.filter(pk=pk).get()
    if post_to_delete:
        if post_to_delete.image:
            post_to_delete.image.delete()
        post_to_delete.delete()
        response['status'] = 'Post successfully deleted!'
        return JsonResponse(data=response)
    else:
        response['status'] = 'Post has not been deleted!'
        return JsonResponse(data=response)


def like(request):
    response = {'likes': '', 'error': ''}
    identifier = request.GET.get('post_id')
    user = request.user
    if user.is_authenticated:
        if identifier:
            post = Post.objects.filter(pk=identifier).get()
            if user in post.likes.all():
                post.likes.remove(user)
            else:
                post.likes.add(user)
            response['likes'] = post.likes.count()
            return JsonResponse(data=response)
        else:
            response['error'] = 'Post ID not found.'
            return JsonResponse(data=response)
    response['error'] = 'You are not logged in!'
    return JsonResponse(data=response)
