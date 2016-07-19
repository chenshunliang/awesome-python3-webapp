from django.contrib import admin
from dtest.models import Person


# Register your models here.
class PersonAdmin(admin.ModelAdmin):
    list_display = ('name', 'age',)
    search_fields = ('name',)


admin.site.register(Person, PersonAdmin)
