from django import forms
from ..models import SmsSend

class SmsForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['msg_getter'].required = True
        self.fields['msg_text'].required = True

    class Meta:
        model = SmsSend
        fields = (
            'msg_type',
            'msg_getter',
            'msg_sender',
            'msg_text',
        )
