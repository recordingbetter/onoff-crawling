from django.shortcuts import redirect, render

from member.models import MyUser
from ..forms import UserEditForm

__all__ = (
    'my_profile',
    'profile_edit',
    'profile_delete',
)


def my_profile(request):
    if not request.user.is_authenticated:
        return redirect('member:login')
    user = request.user
    context = {
        'user': user,
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


def profile_delete(request):
    if request.method == "POST":
        user = MyUser.objects.get(pk=request.user.id)
        user.delete()
        return redirect('member:signup')
    else:
        pass
