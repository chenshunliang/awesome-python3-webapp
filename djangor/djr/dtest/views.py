# coding:utf-8

from django.shortcuts import render
from django.http import HttpResponse


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
