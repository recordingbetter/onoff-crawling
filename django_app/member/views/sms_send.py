# Create your views here.
import sys

from django.http import HttpResponse
from django.shortcuts import render, redirect
from sdk.api.message import Message
from sdk.exceptions import CoolsmsException

from member import apis
from ..apis import api_key, api_secret
from ..forms import SmsForm

__all__ = (
    'sms_send',
)


def sms_send(request):
    form = SmsForm(data=request.POST)

    def get_valid_sms_info_and_save():
        get_valid_params = {
            'type': 'sms',
            'to': apis.api_default_getter,
            'from': apis.api_owner_num,
            'text': '새로운 컨퍼런스 소식이 있습니다.',
        }
        if form.is_valid():
            form.save()
        return get_valid_params

    if request.method == "POST":
        try:
            params = get_valid_sms_info_and_save()
            cool = Message(api_key, api_secret)
            response = cool.send(params)
            success_count = response['success_count']
            print(success_count)
            error_count = response['error_count']
            print(error_count)
            print('Group ID : {}'.format(response['group_id']))

            if 'error_list' in response:
                print('Error List : {}'.format(response['error_list']))
            context = {
                'form': form,
                'success_count': success_count,
                'error_count': error_count,
            }
            return render(request, 'member/my_profile.html', context)

        except CoolsmsException as e:
            return HttpResponse('Error : {} - {}'.format(e.code, e.msg))
    else:
        form = SmsForm()
    context = {
        'form': form,
    }
    return render(request, 'member/my_profile.html', context)
