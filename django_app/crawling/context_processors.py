from .forms import LoginForm, SignupForm


def forms(request):
    context = {
        'signup_form': SignupForm(),
        'login_form': LoginForm(),
    }
    return context