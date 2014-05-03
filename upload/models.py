from django.db import models
from django.forms import ModelForm

# Create your models here.

class user_details(models.Model):
    user_name=models.CharField(max_length = 50, primary_key=True)
    full_name=models.CharField(max_length = 50)
    email=models.EmailField(max_length = 50)
    password=models.CharField(max_length = 50)
    phone=models.IntegerField(max_length = 10)
    state=models.CharField(max_length = 50)
    image=models.ImageField(upload_to=".")
    
    def __unicode__(self):
           return  unicode(self.user_name)+ unicode(self.password)+ unicode(self.image)   

# Model for subject  
class subject_details(models.Model):
    subject_name=models.CharField(max_length = 50)
    subject_id=models.IntegerField(max_length = 10, primary_key=True)
    class_name=models.ForeignKey('class_details')
    def __unicode__(self):
           return  unicode(self.class_name)   
# Model for Chapters   
class chapter_details(models.Model):
    chapter_name=models.CharField(max_length = 50)
    chapter_id=models.IntegerField(max_length = 10, primary_key=True)
    subject_id=models.ForeignKey('subject_details')
    def __unicode__(self):
           return unicode(self.chapter_id)   
# Model for classes
class class_details(models.Model):
    class_name=models.CharField(max_length = 50, primary_key=True)
    class_id=models.IntegerField()
    def __unicode__(self):
           return  unicode(self.class_name)   

# Mdoel for lecture notes
class lecture_notes(models.Model):
    class_name=models.ForeignKey('class_details')
    subject_id=models.ForeignKey('subject_details')
    chapter_id=models.ForeignKey('chapter_details')
    path=models.FileField(upload_to= '.')
    def __unicode__(self):
           return  unicode(self.class_name)+ unicode(self.subject_id)+ unicode(self.chapter_id)   

