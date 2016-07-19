# coding:utf-8

from django.shortcuts import render
from django.http import HttpResponse
from dtest.models import Person


# Create your views here.

def index(request):
    return HttpResponse(u'进行django测试')


def add(request):
    a = request.GET['a']
    b = request.GET['b']
    c = int(a) + int(b)
    return HttpResponse(str(c))


def add2(request, a, b):
    c = int(a) + int(b)
    return HttpResponse(str(c))


def home(request):
    colorList = ['red', 'white', 'blue']
    return render(request, 'dtest/home.html', {'string': 'aaaaa', 'colors': colorList})


def create_peo(request, name, age):
    # if not isinstance(age, int):
    #     return HttpResponse(status=403)
    p = Person(name=name)
    p.age = int(age)
    p.save()
    return HttpResponse(str('ok'))


def get_all(request):
    pList = Person.objects.all()
    s = ''
    for p in pList:
        s += 'name:{0},age:{1}.\r'.format(p.name, len(str(p.age)))
    return HttpResponse(s)
