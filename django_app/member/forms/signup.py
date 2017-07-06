import re

from django import forms
from ..models import MyUser
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
    slack = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                'placeholder': 'example@example.com (필수입력)',
            }
        )
    )
    phone = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder': '문자알림을 받을 휴대폰 번호를 숫자만 입력하세요 (필수입력)',
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

    def clean_slack(self):
        slack = self.cleaned_data.get('slack')
        if slack and slack in MyUser.objects.get(slack=slack).exists():
            raise forms.ValidationError('이미 등록된 슬랙 계정입니다.')
        return slack

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        phone_strip = re.compile(r'^[0-9]{2,3}[-.][0-9]{3,4}[-.][0-9]{4}$')
        phone_number = phone_strip.search(phone)
        phone_val = phone_number.group()
        if phone_val and phone_val in MyUser.objects.get(phone=phone_val).exists():
            raise forms.ValidationError('이미 등록된 전화번호입니다.')
        return phone_val

    def create_user(self):
        username = self.cleaned_data['username']
        nickname = self.cleaned_data['nickname']
        password = self.cleaned_data['password1']
        slack = self.cleaned_data['slack']
        phone = self.cleaned_data['phone']
        new_user = MyUser.objects.create_user(
            username=username,
            nickname=nickname,
            password=password,
            slack=slack,
            phone=phone,
        )
        return new_user

