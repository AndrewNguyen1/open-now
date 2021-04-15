from django.forms import ModelForm
from .models import *
from django import forms
 
class CreateInForum(ModelForm):
    class Meta:
        model= Forum
        fields = ['topic', 'description']
 
class CreateInDiscussion(ModelForm):
    class Meta:
        model= Discussion
        fields = "__all__"

class BusinessImageForm(ModelForm):
    class Meta:
        model = Business
        fields = ['business_image']
        widgets = {'business_image': forms.ClearableFileInput(attrs={'class': 'form-control mt-2 mb-4'})}

class CreateBusinessForm(ModelForm):
    class Meta:
        model = Business
        fields = ['business_name','description','website','phone_number','business_category']