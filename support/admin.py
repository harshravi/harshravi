from django.contrib import admin
from support.models import customer_details, complaint_details



# Register your models here.


   
class complaint_details_Admin(admin.ModelAdmin):
    list_display=('complaint_id','customer_id','complaint_date','complaint','complaint_status')
    search_fields=('complaint_id','customer_id')
    list_filter=('complaint_id', 'customer_id')
    


class customer_details_Admin(admin.ModelAdmin):    
    list_display=('customer_id','customer_name','phone','Email')
    search_fields=('customer_name','customer_id')
    list_filter=('customer_id', 'customer_name')




  
    
admin.site.register(customer_details,customer_details_Admin)
admin.site.register(complaint_details,complaint_details_Admin) 

   
