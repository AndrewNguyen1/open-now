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
	business_image = models.ImageField(upload_to = 'media/', blank = True, null = True)

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


