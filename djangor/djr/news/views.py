from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from .models import Column, Article
from django.core import urlresolvers
import json


# Create your views here.

def add_info(request):
    columns_urls = [
        ('体育新闻', 'sports'),
        ('社会新闻', 'society'),
        ('科技新闻', 'tech'),
    ]

    for column_name, url in columns_urls:
        c = Column.objects.get_or_create(name=column_name, slug=url)[0]

        # 创建 10 篇新闻
        for i in range(1, 11):
            article = Article.objects.get_or_create(
                title='{}_{}'.format(column_name, i),
                slug='article_{}'.format(i),
                content='新闻详细内容： {} {}'.format(column_name, i)
            )[0]

            article.column.add(c)
    return HttpResponse(str('OK'))


def add(request, a, b):
    return JsonResponse({'a': a, 'b': b, 'a+b=': int(a) + int(b)}, safe=False)


# 内部跳转
def reverse(request):
    u = urlresolvers.reverse(add, args=(12, 23,))
    return HttpResponseRedirect(u)


def vue(request):
    data = {'name': 'chen', 'age': 18, 'class': 'red', 'ok': True, 'listUser': ['c', 'd', 'e']}
    return render(request, 'news/vuetest.html', {'u': json.dumps(data)})
