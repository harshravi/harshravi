from django import forms
from django.forms import ModelForm
from upload.models import *

class lecture_notes_upload(forms.Form):
	class_name = forms.ModelMultipleChoiceField(queryset=class_details.objects.all())
	subject_id = forms.CharField(label="Select subject")
	chapter_id = forms.CharField(label="Select chapter")
	files = forms.FileField()
