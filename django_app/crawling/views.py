import re

import requests
from django.core.files import File
from django.core.files.temp import NamedTemporaryFile
from django.db.models import Q
from django.shortcuts import render

from .forms import SearchForm
from .models import News

import requests
from bs4 import BeautifulSoup


def crawling(keyword):

    ### seleium ###
    # from selenium import webdriver
    # ff_driver = webdriver.Firefox()
    # ff_driver.get("http://onoffmix.com/event?s=" + keyword)
    # ff_driver.find_element_by_class_name("soon").click()
    # elements = ff_driver.find_elements_by_class_name("todayEvent")

    ### bs4 ###
    r = requests.get("http://www.onoffmix.com/event?s=" + keyword, headers={
         'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:10.0.2) Gecko/20100101 Firefox/10.0.2',
    })
    ### mac ###
    # 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'

    soup = BeautifulSoup(r.text, 'html.parser')
    elements = soup.find_all('ul', class_='todayEvent')[:10]

    return elements


def slack_chat():
    pass


def news_get_or_create(user, keyword):
    ### selenium ###
    # new_datas = selenium(keyword)[:10]
    # for i in new_datas:
    #     thumbnail = i.find_element_by_class_name("thumbnail").get_attribute('src')
    #     title = i.find_element_by_class_name("eventLink").get_attribute('title')
    #     detail_link = i.find_element_by_class_name("eventLink").get_attribute('href')

    ### bs4 ###
    datas = crawling(keyword)
    for data in datas:
        thumbnail = data.img['src']
        title = data.img['alt']
        detail_link = data.a['href']

        # print(thumbnail, "-", title, "-", detail_link)

        News.objects.get_or_create(
            user=user,
            title=title,
            detail_link=detail_link,
            img_news=thumbnail,
        )

    # slack, sms 보내기


def news_list(request):
    datas = News.objects.all().filter(user_id=request.user.id)
    for data in datas:
        print(data)
    context = {
        'datas': datas,
        'search_form': SearchForm()
    }
    return render(request, 'news/news_list.html', context)


def news_search(request):
    form = SearchForm(data=request.POST)
    if form.is_valid():

        q = form.cleaned_data['q_search']

        if request.method == 'POST':
            news_get_or_create(request.user, q)

        datas = News.objects.filter(title__contains=q)
        datas = News.objects.all().filter(user_id=request.user.id)

        context = {
            'datas': datas,
            'search_form': SearchForm(),
        }
        return render(request, 'news/news_search.html', context)
