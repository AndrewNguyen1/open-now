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
	# from https://gist.github.com/sandes/ca4405b996227e49ca00b3f052975347
	US_STATES = (
		('AL','Alabama'),
		('AK','Alaska'),
		('AS','American Samoa'),
		('AZ','Arizona'),
		('AR','Arkansas'),
		('CA','California'),
		('CO','Colorado'),
		('CT','Connecticut'),
		('DE','Delaware'),
		('DC','District of Columbia'),
		('FL','Florida'),
		('GA','Georgia'),
		('GU','Guam'),
		('HI','Hawaii'),
		('ID','Idaho'),
		('IL','Illinois'),
		('IN','Indiana'),
		('IA','Iowa'),
		('KS','Kansas'),
		('KY','Kentucky'),
		('LA','Louisiana'),
		('ME','Maine'),
		('MD','Maryland'),
		('MA','Massachusetts'),
		('MI','Michigan'),
		('MN','Minnesota'),
		('MS','Mississippi'),
		('MO','Missouri'),
		('MT','Montana'),
		('NE','Nebraska'),
		('NV','Nevada'),
		('NH','New Hampshire'),
		('NJ','New Jersey'),
		('NM','New Mexico'),
		('NY','New York'),
		('NC','North Carolina'),
		('ND','North Dakota'),
		('MP','Northern Mariana Islands'),
		('OH','Ohio'),
		('OK','Oklahoma'),
		('OR','Oregon'),
		('PA','Pennsylvania'),
		('PR','Puerto Rico'),
		('RI','Rhode Island'),
		('SC','South Carolina'),
		('SD','South Dakota'),
		('TN','Tennessee'),
		('TX','Texas'),
		('UT','Utah'),
		('VT','Vermont'),
		('VI','Virgin Islands'),
		('VA','Virginia'),
		('WA','Washington'),
		('WV','West Virginia'),
		('WI','Wisconsin'),
		('WY','Wyoming')
	)

	street_address = models.CharField(max_length=200)
	alt_info = models.CharField(max_length=100, null=True, blank=True)
	city = models.CharField(max_length=50)
	state = models.CharField(max_length=2,choices=US_STATES)
	postal_code = models.IntegerField()

	def __str__(self):
		return f"Location is {self.street_address} ({self.alt_info}) {self.city}, {self.state} {self.postal_code}"



class Search(models.Model):
	CATEGORIES = (
		('REST','Restaurant'),
		('SHOP','Retail'),
		('GYM','Gym or Workout'),
		('NONE','Other or Unspecified')
	)

	search_name = models.CharField(max_length=50)
	radius = models.IntegerField()

	"""class SearchCategory(models.TextChoices):
		RESTAURANT = 'REST', _('Restaurant')
		RETAIL = 'SHOP', _('Retail')
		GYM = 'GYM', _('Gym or Workout')
		OTHER = 'NONE', _('Other or Unspecified')"""

	"""search_category = models.CharField(
		max_length = 4,
		choices = SearchCategory.choices,
		default = SearchCategory.OTHER,
	)"""

	search_category = models.CharField(max_length=4,choices=CATEGORIES,default=('NONE','Other or Unspecified'))

	def __str__(self):
		return f"{self.business_name} - {self.radius} km"