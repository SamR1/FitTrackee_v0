from django.contrib import admin

from .models import Activity, Sport, Gpx, Comment


admin.site.register(Activity)
admin.site.register(Sport)
admin.site.register(Gpx)
admin.site.register(Comment)
