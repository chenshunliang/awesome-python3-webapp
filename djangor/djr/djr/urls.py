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
from django.conf.urls import url, include
from django.contrib import admin

from dtest import views as test_view
from news import views as new_view
from django.contrib.sitemaps import GenericSitemap
from django.contrib.sitemaps.views import sitemap
from news.admin import admin as nadmin
from dtest.admin import admin as dadmin

# sitemap = {
#
# }

urlpatterns = [
    url(r'^homeeee/$', test_view.home, name='home2'),
    url(r'^add/$', test_view.add),
    # url(r'^add/(\d+)/(\d+)$', test_view.add2, name='add2'),
    url(r'^admin/', include(nadmin.site.urls)),
    # url(r'^dtest/admin/', include(dadmin.site.urls)),
    url(r'^create/(\w+)/(\d+)$', test_view.create_peo),
    url(r'^get_peo/$', test_view.get_all),
    url(r'^add_user/$', test_view.add_user, name='post'),
    # url(r'^accounts/', include('users.urls')),
    url(r'^get_json/$', test_view.ajax_json),
    url(r'^add_info/$', new_view.add_info),
    # 捕捉值参数
    url(r'^add/(?P<a>\d+)/(?P<b>\d+)$', new_view.add),
    url(r'^r$', new_view.reverse),
    url(r'^testvue$', new_view.vue),
]
