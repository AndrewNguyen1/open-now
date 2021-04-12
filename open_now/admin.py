from django.contrib import admin

# Register your models here.

from .models import Business, Forum, Discussion, Location, Search

admin.site.register(Business)
admin.site.register(Forum)
admin.site.register(Discussion)
admin.site.register(Location)
admin.site.register(Search)