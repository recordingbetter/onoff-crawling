import re

import requests
from django.core.files import File
from django.core.files.temp import NamedTemporaryFile
from django.db.models import Q
from django.shortcuts import render

from .forms import SearchForm
from .models import News


def selenium(keyword):
    from selenium import webdriver

    print(keyword)
    ff_driver = webdriver.Firefox()
    ff_driver.get("http://onoffmix.com/event?s=" + keyword)

    # ff_driver.find_element_by_class_name("soon").click()

    elements = ff_driver.find_elements_by_class_name("todayEvent")

    return elements


def news_get_or_create(user, q):
    new_datas = selenium(q)[:10]

    for i in new_datas:
        thumbnail = i.find_element_by_class_name("thumbnail").get_attribute('src')
        title = i.find_element_by_class_name("eventLink").get_attribute('title')
        detail_link = i.find_element_by_class_name("eventLink").get_attribute('href')

        print(thumbnail, title, detail_link)

<<<<<<< Updated upstream
        news, news_create = News.objects.get_or_create(
=======
        alram, alram_value = News.objects.get_or_create(
>>>>>>> Stashed changes
            user=user,
            title=title,
            detail_link=detail_link,
            # img_news=thumbnail,
        )

<<<<<<< Updated upstream
        # 새로운레코드가 생겼으면
        if news_create:
            # 이미지 저장
            # p = re.compile(r'.*\.([^?]+)')
            # file_ext = re.search(p, thumbnail).group(1)
            file_name = '{}.{}'.format(
                    news.id,
                    'jpg'
                    )
            temp_file = NamedTemporaryFile()
            response = requests.get(thumbnail)
            temp_file.write(response.content)
            news.img_news.save(file_name, File(temp_file))

            # slack, sms 보내기
            pass
=======
        alram = q + "에 대한 정보가 업데이트됐습니다."
        if alram_value == True:
            slack_chat(alram)

>>>>>>> Stashed changes


def news_list(request):

    datas = News.objects.filter(pk=request.user.id)

    context = {
        'datas': datas,
        'search_form': SearchForm()
    }
    return render(request, 'news/news_list.html', context)


def slack_chat(alram):
    token = 'xoxb-209889657046-ktg9cEnF9LUDLobDpCg2yryM'

    from slacker import Slacker
    slack = Slacker(token)

    slack.chat.post_message('#test', alram)


def news_search(request):
<<<<<<< Updated upstream
    if request.method == "POST":
=======
    if request.method == 'POST':
>>>>>>> Stashed changes
        form = SearchForm(data=request.POST)
        if form.is_valid():

            q = form.cleaned_data['q_search']

            news_get_or_create(request.user, q)

            datas = News.objects.filter(title__contains=q)

            context = {
                'datas': datas,
                'search_form': SearchForm(),
            }
            return render(request, 'news/news_search.html', context)
<<<<<<< Updated upstream
    else:
        datas = News.objects.filter(title__contains=q)
        context = {
            'datas': datas,
            }
        return render(request, 'news/news_search.html', context)
=======
>>>>>>> Stashed changes
