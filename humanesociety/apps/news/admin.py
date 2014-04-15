from django.contrib import admin

from apps.news.models import Entry

class EntryAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug': ('title', ),
    }

    

admin.site.register(Entry, EntryAdmin)
