from django import forms
from member.models import MyUser


class UserEditForm(forms.ModelForm):
    class Meta:
        model = MyUser
        fields = [
            'username',
            'password',
            'img_profile',
            'nickname',
            'slack',
            'phone',
        ]
