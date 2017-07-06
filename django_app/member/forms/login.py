from django import forms
from django.contrib.auth import authenticate


class LoginForm(forms.Form):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('label_suffix', '')
        super().__init__(*args, **kwargs)

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
                '로그인 정보가 부정확합니다. 다시 로그인하시거나, 회원가입해주세요.'
            )
        return self.cleaned_data
