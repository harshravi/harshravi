from django.db import models

# Create your models here.

#Class for subject's details

class subject_details(models.Model):
        subject_name = models.CharField(max_length=50)
        models.AutoField(primary_key=True)
        def __unicode__(self):
                        return  unicode(self.subject_name) +" / " +  unicode( self.subject_id)

# Class for chapter's details

class chapter_details(models.Model):
        chapter_name = models.CharField(max_length=50)
        chapter_id = models.AutoField(primary_key=True)
        def __unicode__(self):
               return  unicode( self.chapter_name) +" / " +  unicode( self.chapter_id)





