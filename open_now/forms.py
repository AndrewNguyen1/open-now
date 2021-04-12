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

class LocationForm(ModelForm):
	class Meta:
		model = Location
		fields = ['street_address', 'alt_info', 'city', 'state', 'postal_code']

class SearchForm(ModelForm):
	class Meta:
		model = Search
		fields = ['search_name', 'radius']