from django.db import models
from django.utils.encoding import python_2_unicode_compatible


# Create your models here.

# 适应python2.x
@python_2_unicode_compatible
class Person(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField(default=10)

    def __str__(self):
        return self.name
