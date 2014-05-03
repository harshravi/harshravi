from django.db import models

# Create your models here.

class user_details(models.Model):
	user_name = models.CharField(primary_key=True, max_length=50)
	full_name = models.CharField(max_length=50)
	password  = models.CharField(max_length=50)
	phone = models.IntegerField()
	email = models.EmailField()
	def __unicode__(self):
		return self.full_name +" / " + self.user_name +" / " + unicode(self.date_of_joining) +" / " + self.email +" / "


