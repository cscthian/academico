# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Category, Entry, Sugerencia, Subscription


# class EntryAdmin(admin.ModelAdmin):
#     list_display = ('pk','title','created')
#     search_fields = ('title', 'content')
#     filter_horizontal = ('category',)

#admin.site.register(Entry, EntryAdmin)

admin.site.register(Category)
admin.site.register(Entry)
admin.site.register(Sugerencia)
admin.site.register(Subscription)
