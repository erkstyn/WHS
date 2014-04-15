from django.contrib import admin

from .models import Entry


class EntryAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug': ('title', ),
    }

    radio_fields = {
        'status': admin.VERTICAL,
    }

    list_display = (
        'title',
        'status',
        'date_created',
    )

    list_filter = (
        'title',
        'status',
        'date_created',
    )

    

admin.site.register(Entry, EntryAdmin)
