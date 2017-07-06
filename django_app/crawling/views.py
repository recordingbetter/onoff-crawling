from django.shortcuts import render
from .models import News


def selenium(keyword):
    from selenium import webdriver

    print(keyword)
    ff_driver = webdriver.Chrome()
    ff_driver.get("http://onoffmix.com/event?s=" + keyword)

    # ff_driver.find_element_by_class_name("soon").click()

    elements = ff_driver.find_elements_by_class_name("todayEvent")

    return elements


def news_list(request, user_id):
    # News 모델 객체
    datas = News.objects.filter(pk=user_id)

    # 크롤링한 객체
    new_datas = selenium("빅데이터")[:10]

    for i in new_datas:
        thumbnail = i.find_element_by_class_name("thumbnail").get_attribute('src')
        title = i.find_element_by_class_name("eventLink").get_attribute('title')
        detail_link = i.find_element_by_class_name("eventLink").get_attribute('href')

        print(thumbnail, title, detail_link)

        News.objects.get_or_create(
            user=request.user,
            title=title,
            detail_link=detail_link,
            img_news=thumbnail,
        )
        print(News.objects.last().title)

    datas = News.objects.filter(pk=user_id)

    context = {
        'datas': datas,
    }
    return render(request, 'news/news_list.html', context)
