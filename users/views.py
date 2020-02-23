from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.messages import success, info, warning
from django.shortcuts import redirect
from django.contrib.auth import login, authenticate, logout, get_user_model
from django.contrib.auth.decorators import login_required
from .forms import UpdateProfileForm, UserEditForm
from .models import Profile
from django.views.generic import DetailView, DeleteView
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.http import HttpResponseRedirect
from users.forms import UserRegisterForm


def register_view(request):
    if request.method == 'POST':
        new_user = UserRegisterForm(request.POST)
        if new_user.is_valid():
            new_user.save()
            success(request=request, message=str(request.POST.get('username')) + ', you have successfully registered!')
            return redirect(to='login')
    else:
        new_user = UserRegisterForm()
    return render(request=request, template_name='users/register.html', context={'reg_form': new_user})


def login_view(request):
    if request.method == 'POST':
        af = AuthenticationForm(request, data=request.POST)
        if af.is_valid():
            username = request.POST.get('username')
            user = authenticate(request=request,
                                username=username,
                                password=request.POST.get('password'))
            login(request=request, user=user)
            success(request=request, message='Welcome, ' + username + ' !')
            return redirect(to='homepage')
    else:
        af = AuthenticationForm()
    return render(request=request, template_name='users/login.html', context={'login_form': af})


def logout_view(request):
    if str(request.user) == 'AnonymousUser':
        info(request=request, message='You cannot logout because You are not logged in!')
    else:
        logout(request=request)
        info(request=request, message='You are now logged out.')
    return render(request=request, template_name='users/logout.html')


class ProfileDetailView(DetailView):
    model = Profile


@login_required
def profile_update_view(request, pk: int):
    filtered_user = get_user_model().objects.filter(pk=pk)
    user = filtered_user.get()
    if request.user.pk == user.pk:
        if request.method == 'POST':
            u = UserEditForm(request.POST, instance=user)
            p = UpdateProfileForm(request.POST, files=request.FILES, instance=user.profile)
            if u.is_valid() and p.is_valid():
                u.save()
                p.save()
                success(request=request, message='Profile successfully updated.')
                return redirect(to='profile-detail', pk=user.profile.pk)
            elif len(str(user)) < 5:
                user = filtered_user.get()
        else:
            u = UserEditForm(initial={'username': user.username, 'email': user.email})
            p = UpdateProfileForm(initial={'image': user.profile.image})
        return render(request=request,
                      template_name='users/profile_update.html',
                      context={
                          'profile_update_form': p,
                          'user_update_form': u,
                          'view': {
                              'pk': pk,
                              'user': user
                          }
                      })
    else:
        warning(request=request, message="You cannot edit somebody's profile!")
        return redirect(to='homepage')


class AccountDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = get_user_model()
    success_url = '/'
    user = ''

    def delete(self, request, *args, **kwargs):
        if not self.user.profile.image == 'profile_pics/profile.png':
            self.user.profile.image.delete()
        super().delete(request=request, args=args, kwargs=kwargs)
        info(request=request, message='You have successfully deleted your account.')
        return HttpResponseRedirect(redirect_to=self.get_success_url())

    def test_func(self):  # when False 403 Forbidden
        self.user = self.get_object()
        if self.user == self.request.user:
            return True
        return False
