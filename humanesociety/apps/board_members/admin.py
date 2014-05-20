from django.contrib import admin

from .models import BoardMember

class BoardMemberAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'title',
        'email',
        'phone',
    )

    search_fields = (
        'name',
        'title',
    )

admin.site.register(BoardMember, BoardMemberAdmin)
