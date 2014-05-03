from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context
import datetime
from django.template.loader import get_template
from django.shortcuts import render_to_response
from upload.forms import lecture_notes_upload
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
from django.core.context_processors import csrf
from django.views.decorators.csrf import csrf_exempt
from .forms import lecture_notes_upload
from upload.models import *

# Create your views here.
@csrf_exempt
def upload(request):
    if request.method == 'POST':
        form = lecture_notes_upload(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file = request.FILES['files']
            fout = open("/home/sonu/django-thinkiit/thinkiit/uploaded_files/notes/%s" % uploaded_file.name, 'wb')
            for chunk in uploaded_file.chunks():
                fout.write(chunk)
                fout.close()
            class_name=request.POST.get('class_name')
            sub_id= request.POST.get('subject_id')
            chap_id= request.POST.get('chapter_id')
            files=('/home/sonu/django-thinkiit/thinkiit/uploaded_files/notes/' + uploaded_file.name)
            post=lecture_notes(class_name=class_name, subject_id = sub_id,chapter_id= chap_id,  files= files )
            post.save()
            return HttpResponse('SUCCESS! :)')
        else:
        	form = lecture_notes_upload()
    return render_to_response('upload.html', {'form':lecture_notes_upload() })


