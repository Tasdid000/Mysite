from .models import *
from django.contrib import admin

# Register your models here.

@admin.register(portfolio)
class portfolioAdmin(admin.ModelAdmin):
    class Media:
        js = ('tiny.js',)
admin.site.register(allimage)
