from django.shortcuts import render
from django.template import RequestContext
from django.http import HttpResponse
from django.template import Template, Context
import datetime
#from home.models import user_details
from upload.models import user_details
from django.template.loader import get_template
from django.shortcuts import render_to_response
from django.core.context_processors import csrf
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def base(request):
     t = get_template('base.html')
     return HttpResponse(t)

def current_datetime(request):
    now = datetime.datetime.now()
    t =get_template('current_datetime.html')
    return HttpResponse(t)

def home(request):
    return render_to_response('index.html')

def video(request):
    return render_to_response('video.html')

def admins(request):
    return render_to_response('admin_login.html')

def contact(request):
    return render_to_response('contact_us.html')

def branch_selector(request):
    return render_to_response('branch_selector.html')

def about_us(request):
    return render_to_response('about_us.html')

def term_cond(request):
    return render_to_response('term_cond.html')

def privacy_policy(request):
    return render_to_response('privacy_policy.html')

def cancellation_return(request):
    return render_to_response('cancellation_return.html')

def user(request):
	if request.method == 'POST':
             return render_to_response('user_home.html')
	else:
             return render_to_response('index.html')
@csrf_exempt
def adminji(request):
    return render_to_response('admin.html')


def lecture_index(request):
    return render_to_response('lecture_index.html')


@csrf_exempt
def base(request):
    return render_to_response('base.html')

@csrf_exempt
def login(request):
       user=request.POST.get('username')
       password=request.POST.get('password')
      
       if (user == ""):
           return HttpResponse("Please enter User name ")
       if (password == ""):
	    return HttpResponse("Please enter password")
       
       try:  
            user_pic=user_details.objects.get(user_name = user)
            database_usr=user_details.objects.get(user_name = user)
            database_pwd=user_details.objects.get(password = password)
            if user in database_usr.user_name and password in database_pwd.password:
                 return render_to_response('user_home.html',RequestContext(request, {'pic': user_pic}))
       except:
               return HttpResponse("Invalid user name or Password" + "!!" + "Try again")
		#return render_to_response("home.html""Try again")

@csrf_exempt
def signup(request):
       username=request.POST.get('user_name')
       name=request.POST.get('name')
       password=request.POST.get('pwd')
       cpassword=request.POST.get('cpassword')	
       email=request.POST.get('email')
       #print("username:" + unicode(username) + "name:" + name +"pwd:" + password + "cpwd:" + cpassword + "email:" + email)
       if (username == "") or (name == "") or (email == "") or (password == "") or (cpassword == ""):
           return HttpResponse("You missed some Entries!! ")
       elif (password == cpassword):
             s1=user_details(user_name = username,full_name= name, password= cpassword, email=email, date_of_joining='2014-12-12' )
             s1.save()
             return HttpResponse("Data validation successful!!" +"Welcome Mr."+ name)
             
       else:
	    return HttpResponse("Password Mismatched")
      
def jee(request):
      return render_to_response('notes_list.html')

def search(request):
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        
        return render(request, 'search.html',
            {'query': q})
    else:
        return HttpResponse('Please submit a search term.')


def phy_index(request):
	return render_to_response('phy_index.html')

def chem_index(request):
	return render_to_response('chem_index.html')

def maths_index(request):
	return render_to_response('maths_index.html')

def test(request):
	return render_to_response('test.html')

def classes(request):
	return render_to_response('class.html')

def solution(request):
	return render_to_response('solution.html')

