from django.forms import ModelForm
from .models import *
 
class CreateInForum(ModelForm):
    class Meta:
        model= Forum
        fields = ['topic', 'description']
 
class CreateInDiscussion(ModelForm):
    class Meta:
        model= Discussion
        fields = ['discuss']

class CreateInHours(ModelForm):
    class Meta:
        model= OpeningHours
        fields = ["weekday_from", "weekday_to", "from_hour", "to_hour"]
        
class LocationForm(ModelForm):
	class Meta:
		model = Location
		fields = ['street_address', 'address_2', 'city', 'state', 'postal_code']

class SearchForm(ModelForm):
	class Meta:
		model = Search
		fields = ['search_category', 'radius']
