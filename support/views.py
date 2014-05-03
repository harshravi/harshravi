from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context
import datetime
from support.models import customer_details
from django.template.loader import get_template
from django.shortcuts import render_to_response
from django.core.context_processors import csrf
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def ua_display(request):
    ua = request.META.get('HTTP_USER_AGENT', 'unknown')
    return HttpResponse("Your browser is %s" % ua)
def support(request):
	return render_to_response('support.html')
