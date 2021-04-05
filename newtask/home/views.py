from django.shortcuts import render
from home.models import User

# Create your views here.
from django.http import JsonResponse
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from .decorators import user_task
from django.views.generic import TemplateView, ListView
from .models import City
from django.db.models import Q
from .forms import UserAddForm




def lobby(request):
	cityobject = City.objects.filter().all()
	search = request.GET.get('search')
	if search:
		cityobject = cityobject.filter(Q(name__icontains=search) | Q(state__icontains=search))
	return render(request, 'lobby.html',{'cityobject':cityobject})

# class SearchResultsView(ListView):
#     model = City
#     template_name = 'search_results.html'
#     def get_queryset(self):
#         query = self.request.GET.get('q')
#         return City.objects.filter(Q(name__icontains=query) | Q(state__icontains=query))

@user_task
def registration(request):
	"""
	This function is created for User registration
	"""
	choices = ['Employee','Student','Manager']
	# print(entry,'ppppppppppppppp')
	if request.method == 'POST':
		# registration_form = RegisterationForm(request.POST)
		name = request.POST.get('name')
		mobile = request.POST.get('mobile_number_form')
		emaill = request.POST.get('email')
		user_type = request.POST.get('choices')
		
		# pvurl = Site.objects.get_current()
		# pvurlstr = str(pvurl)
		# pvnew = mobile + pvurlstr 
		register = User.objects.create( username = name, mobile = mobile,user_type=user_type,first_name = name, email = emaill)
		register.set_password('puertevisual')
		register.save()

	return render(request, 'registration.html',{'choices':choices})

def login(request):
	"""
	This Funcrion is created for User login
	"""
	if request.method == 'POST':
		email = request.POST.get('email')
		password = request.POST.get('password', 'puertevisual')
		mobile = request.POST.get('mobile')
		if User.objects.filter(mobile = mobile).first() and mobile:
			if User.objects.filter(mobile = mobile).first().check_password(str(password)) == True:
				return render(request, 'lobby.html')
			else:
				messages.info(request, 'Please Enter correct password ')
				return HttpResponseRedirect(request.path_info)
		else:
			messages.info(request, 'Enter valid Email')
			return HttpResponseRedirect(request.path_info)
	else:
		pass
	return render(request, 'login.html')

def AddUser(request):
	form = UserAddForm()
	return render(request,'user_add.html',{'form':form})