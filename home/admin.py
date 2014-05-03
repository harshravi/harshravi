from django.contrib import admin
from home.models import chapter_details, user_details, subject_details, notes_details

# Register your models here.

    
class subject_details_Admin(admin.ModelAdmin):    
    list_display=('subject_id','subject_name')
    
class user_details_Admin(admin.ModelAdmin):
    list_display=('user_name','password','email')
    search_fields=('full_name','user_name')
    list_filter=('full_name', 'user_name')
class chapter_details_Admin(admin.ModelAdmin):    
    list_display=('chapter_id','chapter_name')
    search_fields=('chapter_name','chapter_id')
    list_filter=('chapter_id', 'chapter_name')

class notes_details_Admin(admin.ModelAdmin):    
    list_display=('chapter','subject')
    search_fields=('chapter','subject')
    list_filter=('chapter','subject')
    
    
admin.site.register(subject_details, subject_details_Admin)
admin.site.register(user_details,  user_details_Admin) 
admin.site.register(notes_details,  notes_details_Admin)
admin.site.register(chapter_details, chapter_details_Admin)
   
    
