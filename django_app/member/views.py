from django.contrib.auth import login as django_login
from django.shortcuts import render, redirect

# Create your views here.
from member.forms import SignupForm, LoginForm


def signup(request):
    if request.method == "POST":
        form = SignupForm(data=request.POST)
        if form.is_valid():
            user = form.create_user()
            django_login(request, user)
            return redirect('member:my_profile')
        else:
            context = {
                'form': form,
            }
            return render(request, 'member/signup.html', context)
    form = SignupForm()
    context = {
        'form': form,
    }
    return render(request, 'member/signup.html', context)


def login(request, user_pk):
    if request.method == "POST":
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.cleaned_data['user']
            django_login(request, user)
            return redirect('')
