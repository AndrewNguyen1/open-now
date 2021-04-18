from django.forms import ModelForm
from .models import *
 
class CreateInForum(ModelForm):
    class Meta:
        model= Forum
        fields = ['topic', 'description']
 
class CreateInDiscussion(ModelForm):
    class Meta:
        model= Discussion
        fields = "__all__"

class CreateInHours(ModelForm):
    class Meta:
        model= OpeningHours
        fields = ["weekday_from", "weekday_to", "from_hour", "to_hour"]
        fields = ['discuss']
