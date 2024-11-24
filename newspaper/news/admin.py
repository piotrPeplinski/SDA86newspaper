from django.contrib import admin
from .models import Article


class DisplayDate(admin.ModelAdmin):
    readonly_fields = ('date',)


# Register your models here.
admin.site.register(Article, DisplayDate)
