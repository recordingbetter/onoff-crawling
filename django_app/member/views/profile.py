from django.contrib.auth import authenticate
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse

from member.forms import SignupForm
from member.models import MyUser
from ..forms import UserEditForm

__all__ = (
    'my_profile',
    'profile_edit',
    'profile_delete',
)


def my_profile(request, user_pk=None):
    if not request.user.is_authenticated:
        return redirect('member:login')
    user = request.user
    user_pk = request.user.id
    context = {
        'user': user,
        'user_pk': user_pk,
    }
    return render(request, 'member/my_profile.html', context)


def django_login(request, user):
    pass


def profile_edit(request):
    if request.method == "POST":
        form = UserEditForm(
            request.POST,
            request.FILES,
            instance=request.user
        )
        if form.is_valid():
            form.save()
            username = request.POST['username']
            user = MyUser.objects.get(username=username)
            new_password = request.POST['password']
            user.set_password(new_password)
            user = authenticate(username=username, password=new_password)
            if user is not None:
                django_login(request, user)
            else:
                return HttpResponseRedirect(reverse('member:login'))
            user.save()
            return redirect('member:my_profile')
    else:
        form = UserEditForm(
            instance=request.user
        )
    form = UserEditForm(
        instance=request.user
    )
    context = {
        'form': form,
    }
    return render(request, 'member/profile_edit.html', context=context)


def profile_delete(request):
    if request.method == "POST":
        user = MyUser.objects.get(pk=request.user.id)
        user.delete()
        return redirect('member:signup')
    else:
        pass
