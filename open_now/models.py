from django.db import models
from django.utils.translation import gettext_lazy as _


class Login(models.Model):
	text = models.CharField(max_length=200)

	def __str__(self):
		return self.text

HOUR_OF_DAY_24 = [(i,i) for i in range(1,25)]

WEEKDAYS = [
  (1, _("Monday")),
  (2, _("Tuesday")),
  (3, _("Wednesday")),
  (4, _("Thursday")),
  (5, _("Friday")),
  (6, _("Saturday")),
  (7, _("Sunday")),
]


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

HOUR_OF_DAY_24 = [(i,i) for i in range(1,25)]

WEEKDAYS = [
  (1, _("Monday")),
  (2, _("Tuesday")),
  (3, _("Wednesday")),
  (4, _("Thursday")),
  (5, _("Friday")),
  (6, _("Saturday")),
  (7, _("Sunday")),
]

class OpeningHours(models.Model):
    store = models.ForeignKey(Business, on_delete=models.CASCADE)
    weekday_from = models.PositiveSmallIntegerField(choices=WEEKDAYS, unique=True)
    weekday_to = models.PositiveSmallIntegerField(choices=WEEKDAYS)
    from_hour = models.PositiveSmallIntegerField(choices=HOUR_OF_DAY_24)
    to_hour = models.PositiveSmallIntegerField(choices=HOUR_OF_DAY_24)

    def get_weekday_from_display(self):
        return WEEKDAYS[self.weekday_from]

    def get_weekday_to_display(self):
        return WEEKDAYS[self.weekday_to]

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


class Review(models.Model):

	business = models.ForeignKey(Business, on_delete=models.CASCADE)
	review_text = models.CharField(max_length=200)

	class Rating(models.IntegerChoices):
		(1, 1),
		(2, 2),
		(3, 3),
		(4, 4),
		(5, 5)

	rating = models.IntegerField(choices=Rating.choices, default=5)

	def __str__(self):
		return str(self.rating)



	

