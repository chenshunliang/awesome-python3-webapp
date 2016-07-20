from django.conf import settings as myset
import datetime


def author_name(request):
    return {'author': 'chen'}


def now_date(request):
    return {'now_date': datetime.datetime.now()}
