from django.shortcuts import redirect, render

from member.models import MyUser
from ..forms import UserEditForm

__all__ = (
    'my_profile',
    'profile_edit',
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


def profile_edit(request):
    if request.method == "POST":
        form = UserEditForm(
            request.POST,
            request.FILE,
            instance=request.user
        )
        if form.is_valid():
            form.save()
            return redirect('member:my_profile')
    else:
        form = UserEditForm(
            instance=request.user
        )
    context = {
        'form': form,
    }
    return render(request, 'member/profile_edit.html', context)