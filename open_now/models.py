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



class Measurement(models.Model):
	location = models.CharField(max_length=200)
	destination = models.CharField(max_length=200)
	distance = models.DecimalField(max_digits=10, decimal_places=2)
	created = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return f"Distance from {self.location} to {self.destination} is {self.distance} km"