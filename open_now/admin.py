from django.contrib import admin

# Register your models here.

<<<<<<< Updated upstream
from .models import Business, Forum, Discussion, Location, Search
=======
from .models import *
>>>>>>> Stashed changes

admin.site.register(Business)
admin.site.register(Forum)
admin.site.register(Discussion)
<<<<<<< Updated upstream
=======
admin.site.register(Review)
admin.site.register(OpeningHours)
>>>>>>> Stashed changes
admin.site.register(Location)
admin.site.register(Search)