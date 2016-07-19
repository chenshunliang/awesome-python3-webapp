"""djr URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from dtest import views as test_view

urlpatterns = [
    url(r'^homeeee/$', test_view.home, name='home2'),
    url(r'^add/$', test_view.add),
    url(r'^add/(\d+)/(\d+)$', test_view.add2, name='add2'),
    url(r'^admin/', admin.site.urls),
    url(r'^create/(\w+)/(\d+)$', test_view.create_peo),
    url(r'^get_peo/$', test_view.get_all),
    url(r'^add_user/$', test_view.add_user, name='post')
]
