from django.db import models

# Create your models here.

class customer_details(models.Model):
    customer_id = models.AutoField(primary_key=True)
    customer_name = models.CharField(max_length=50) 
    phone = models.IntegerField()
    Email = models.EmailField()
    def __unicode__(self):
           return  unicode(self.customer_id) +" / " +""+  unicode(self.customer_name)  
class complaint_details(models.Model):
    complaint_id = models.AutoField(primary_key=True)
    complaint_status=models.BooleanField(max_length=50)
    complaint =models.CharField(max_length=1000)
    complaint_date=models.DateTimeField()
    customer_id = models.ForeignKey('Customer_details')



