from django.shortcuts import render
from .models import News


def selenium(keyword):
    from selenium import webdriver

    ff_driver = webdriver.Chrome()
    ff_driver.get("http://onoffmix.com/" + keyword)

    return ff_driver.find_element_by_class_name("soon").click()


def news_list(request, user_id):
    # News 모델 객체
    datas = News.objects.filter(pk=user_id)

    # 크롤링한 객체
    # new_datas = News.objects.filter(pk=user_id)

    # if datas.detail_link != new_datas.detail_link:
    #     datas = News.objects.create(
    #         user=request.user,
    #         title=new_datas.title,
    #         data_link=new_datas.data_link,
    #         img_news=new_datas.img_news,
    #     )

    context = {
        'datas': datas,
    }
    return render(request, 'news/news_list.html', context)
