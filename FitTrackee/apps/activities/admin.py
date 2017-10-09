from django.contrib import admin

from .models import Activity, Sport, Gpx


class SportAdmin(admin.ModelAdmin):
    list_display = ['pk', 'label']


admin.site.register(Activity)
admin.site.register(Sport, SportAdmin)
admin.site.register(Gpx)
