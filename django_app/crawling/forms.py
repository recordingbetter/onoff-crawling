from django import forms
from crawling.models import MyUser
from django.contrib.auth import authenticate


class SignupForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder': '아이디를 입력하세요',
            }
        )
    )
    nickname = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder': '원하시는 닉네임을 입력하세요',
            }
        )
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'placeholder': '비밀번호를 입력하세요',
            }
        )
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'placeholder': '비밀번호를 한번 더 입력하세요',
            }
        )
    )

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if username and username in MyUser.objects.filter(username=username).exists():
            raise forms.ValidationError("해당 아이디는 사용할 수 없습니다. 다른 아이디를 입력하세요.")
        return username

    def clean_nickname(self):
        nickname = self.cleaned_data.get('nickname')
        if nickname and nickname in MyUser.objects.filter(nickname=nickname).exists():
            raise forms.ValidationError("해당 닉네임은 이미 사용중입니다. 다른 닉네임을 입력하세요.")
        return nickname

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("비밀번호가 서로 일치하지 않습니다. 다시 입력해주세요.")

    def create_user(self):
        username = self.cleaned_data['username']
        nickname = self.cleaned_data['nickname']
        password = self.cleaned_data['password1']
        new_user = MyUser.objects.create(
            username=username,
            nickname=nickname,
            password=password,
        )

class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder': '사용자 아이디를 입력하세요',
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'placeholder': '비밀번호를 입력하세요',
            }
        )
    )

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')

        user = authenticate(
            username=username,
            password=password,
        )
        if user is not None:
            self.cleaned_data['user'] = user
        else:
            raise forms.ValidationError(
                'Login credentials not valid'
            )
        return self.cleaned_data


