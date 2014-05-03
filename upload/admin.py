from django.contrib import admin
from upload.models import user_details, subject_details, chapter_details, class_details, lecture_notes



# Register your models here.


   
class user_details_Admin(admin.ModelAdmin):
    list_display=('user_name','image','phone','state','password','email')
   
class subject_details_Admin(admin.ModelAdmin):
    list_display=('subject_name','subject_id')

class chapter_details_Admin(admin.ModelAdmin):
    list_display=('chapter_name','chapter_id')



class lecture_notes_Admin(admin.ModelAdmin):
    list_display=('class_name','subject_id','chapter_id','path')

class class_details_Admin(admin.ModelAdmin):
    list_display=('class_name','class_id')
      

admin.site.register(user_details,user_details_Admin)
admin.site.register(subject_details,subject_details_Admin) 
admin.site.register(chapter_details,chapter_details_Admin) 
admin.site.register(class_details,class_details_Admin) 
admin.site.register(lecture_notes,lecture_notes_Admin) 

   
