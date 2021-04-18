from django.contrib import admin

# Register your models here.

from .models import Business, Forum, Discussion, Review, OpeningHours

admin.site.register(Business)
admin.site.register(Forum)
admin.site.register(Discussion)
admin.site.register(Review)
admin.site.register(OpeningHours)