from django.contrib import admin
from .models import Show, ShowSearchFields#, UserModes#, ShowGroup


class ShowAdmin(admin.ModelAdmin):
    list_display = ("id", "user","id","ShowFungiNotes","slug")
    prepopulated_fields = {"slug": ("id",)}  # new

class ShowSearchFieldsAdmin(admin.ModelAdmin):
    list_display = ("id", "user","id","slug")
    prepopulated_fields = {"slug": ("id",)}  # new


admin.site.register(Show, ShowAdmin)
admin.site.register(ShowSearchFields, ShowSearchFieldsAdmin)

