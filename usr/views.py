from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from django.contrib.auth.decorators import login_required

# Create your views here.
from .forms import CreateUserForm



def registerPage(request):
	if request.user.is_authenticated:
		# return redirect('home')
		return redirect('signup')
	else: 
		form = CreateUserForm()
		if request.method == 'POST':
			form = CreateUserForm(request.POST)
			if form.is_valid():
				form.save()
				user = form.cleaned_data.get('username')
				messages.success(request, 'Account was created for ' + user)

				return redirect('login')
			

		context = {'form':form}
		return render(request, 'usr/registration.html', context)

		# context = {}
		# return render(request, 'usr/registration.html', context)


def loginPage(request):
	if request.user.is_authenticated:
		return redirect('home')
	else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password =request.POST.get('password')

			user = authenticate(request, username=username, password=password)

			if user is not None:
				login(request, user)
				return redirect('home')
			else:
				messages.info(request, 'Username OR password is incorrect')

		context = {}
		return render(request, 'usr/login.html', context)

		# context = {}
		# return render(request, 'usr/login1.html', context)


def landing_page(request):
	return render(request, "usr/trail.html")
	# return render(request, "usr/landing.html")

@login_required(login_url='login')
def home(request):
	
    return render(request, "usr/dashboard.html")
    #return HttpResponse("<h1>Home page</h1>")

def contact(request):
    return render(request, "usr/about.html")
    # return HttpResponse("<h1>About Page</h1>")

def services(request):
    return render(request, "usr/services.html")

def logoutUser(request):
	logout(request)
	return redirect('login')

