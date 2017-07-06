from django.db.models import Q
from django.shortcuts import render

from .forms import SearchForm
from .models import News


def selenium(keyword):
    from selenium import webdriver

    print(keyword)
    ff_driver = webdriver.Chrome()
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

        News.objects.get_or_create(
            user=user,
            title=title,
            detail_link=detail_link,
            img_news=thumbnail,
        )


def news_list(request):

    datas = News.objects.filter(pk=request.user.id)

    context = {
        'datas': datas,
        'search_form': SearchForm()
    }
    return render(request, 'news/news_list.html', context)


def news_search(request):
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

