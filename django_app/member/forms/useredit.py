from django import forms
from member.models import MyUser


class UserEditForm(forms.ModelForm):
    class Meta:
        model = MyUser
        fields = [
            'username',
            'img_profile',
            'nickname',
            'slack',
            'phone',
        ]
