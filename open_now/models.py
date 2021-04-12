from django.db import models
from django.utils.translation import gettext_lazy as _


class Login(models.Model):
	text = models.CharField(max_length=200)

	def __str__(self):
		return self.text


class Business(models.Model):

	business_name = models.CharField(max_length=50)
	description = models.CharField(max_length=200)
	website = models.CharField(max_length=50)
	phone_number = models.CharField(max_length=10)

	class BusinessCategory(models.TextChoices):
		RESTAURANT = 'REST', _('Restaurant')
		RETAIL = 'SHOP', _('Retail')
		GYM = 'GYM', _('Gym or Workout')
		OTHER = 'NONE', _('Other or Unspecified')

	business_category = models.CharField(
		max_length=4,
		choices=BusinessCategory.choices,
		default=BusinessCategory.OTHER,
	)

	def __str__(self):
		return self.business_name

class Forum(models.Model):
    name=models.CharField(max_length=200)
    email=models.CharField(max_length=200,null=True)
    topic= models.CharField(max_length=300)
    description = models.CharField(max_length=1000,blank=True)
    date_created=models.DateTimeField(auto_now_add=True,null=True)
    
    def __str__(self):
        return str(self.topic)
 
#child model
class Discussion(models.Model):
    forum = models.ForeignKey(Forum,blank=True,on_delete=models.CASCADE)
    discuss = models.CharField(max_length=1000)
 
    def __str__(self):
        return str(self.forum)


class Location(models.Model):
	street_address = models.CharField(max_length=200)
	alt_info = models.CharField(max_length=100, null=True, blank=True)
	city = models.CharField(max_length=50)
	state = models.CharField(max_length=50)
	postal_code = models.IntegerField()

	def __str__(self):
		return f"Location is {self.street_address} ({self.alt_info}) {self.city}, {self.state} {self.postal_code}"



class Search(models.Model):

	search_name = models.CharField(max_length=50)
	radius = models.IntegerField()

	class SearchCategory(models.TextChoices):
		RESTAURANT = 'REST', _('Restaurant')
		RETAIL = 'SHOP', _('Retail')
		GYM = 'GYM', _('Gym or Workout')
		OTHER = 'NONE', _('Other or Unspecified')

	search_category = models.CharField(
		max_length = 4,
		choices = SearchCategory.choices,
		default = SearchCategory.OTHER,
	)

	def __str__(self):
		return f"{self.business_name} - {self.radius} km"