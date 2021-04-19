from django.forms import ModelForm
from .models import *
 
class CreateInForum(ModelForm):
    class Meta:
        model = Forum
        fields = ['topic', 'description']
 
class CreateInDiscussion(ModelForm):
    class Meta:
        model = Discussion
        fields = "__all__"

<<<<<<< Updated upstream
class LocationForm(ModelForm):
	class Meta:
		model = Location
		fields = ['street_address', 'alt_info', 'city', 'state', 'postal_code']
=======
class CreateInHours(ModelForm):
    class Meta:
        model= OpeningHours
        fields = ["weekday_from", "weekday_to", "from_hour", "to_hour"]
        
class LocationForm(ModelForm):
	class Meta:
		model = Location
		fields = ['street_address', 'address_2', 'city', 'state', 'postal_code']
>>>>>>> Stashed changes

class SearchForm(ModelForm):
	class Meta:
		model = Search
<<<<<<< Updated upstream
		fields = ['search_name', 'radius', 'search_category']
=======
		fields = ['search_category', 'radius']
>>>>>>> Stashed changes
