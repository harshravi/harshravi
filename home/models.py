from django.db import models

# Create your models here.


# Class for user's information 

class user_details(models.Model):
	user_name = models.CharField(max_length=50)
	full_name = models.CharField(max_length=50)
	password  = models.CharField(max_length=50)
	date_of_joining = models.DateField(blank=True, null=True)
	email = models.EmailField()
	def __unicode__(self):
		return self.full_name +" / " + self.user_name +" / " + unicode(self.date_of_joining) +" / " + self.email +" / "

#Class for subject's details

class subject_details(models.Model):
	subject_name = models.CharField(max_length=50)
	subject_id = models.IntegerField()
	def __unicode__(self):
			return  unicode(self.subject_name) +" / " +  unicode( self.subject_id) 

# Class for chapter's details

class chapter_details(models.Model):
	chapter_name = models.CharField(max_length=50)
        chapter_id = models.IntegerField()
	def __unicode__(self):
	       return  unicode( self.chapter_name) +" / " +  unicode( self.chapter_id)  

# Class for lecture note's details

class notes_details(models.Model):
	chapter = models.ForeignKey(chapter_details)
	subject = models.ForeignKey(subject_details)
	def __unicode__(self):
	      return  unicode( self.chapter) 


