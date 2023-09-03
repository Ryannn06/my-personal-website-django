from django.shortcuts import render, redirect
from .forms import *
from .models import *

from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm

from django.contrib.auth import get_user_model

from django.core.exceptions import PermissionDenied
from django.http import Http404

from django.shortcuts import get_object_or_404

# Create your views here.
def index (request):
	account = get_user_model()

	personal_info = get_object_or_404(account, is_superuser=True)
	context = {
		'personal_info': personal_info,
	}
	return render(request, 'home.html', context)

def user_login (request):
	if request.user.is_authenticated:
		return redirect('/')

	else:
		if request.method == "POST":
			form = AuthenticationForm(request.POST)
			username = request.POST['username']
			password = request.POST['password']

			user = authenticate(username=username, password=password)
			if user:
				login(request, user)
				return redirect('/')

			else:
				return redirect('/login')

		else:
			form = AuthenticationForm()
			context = {'form': form}
			return render(request, 'login.html', context)

def register (request):
	if request.user.is_authenticated:
		return redirect('/')

	else:
		account = get_user_model()
		admin_account = account.objects.filter(is_superuser=True)

		if admin_account.exists():
			raise PermissionDenied()

		else:
			if request.method == "POST":
				form = signup_form(request.POST, request.FILES)

				if form.is_valid():
					form.save()

					return redirect('/')

			else:
				form = signup_form()

			context = {'form':form}
			return render(request, 'register.html', context)


def my_projects(request):
	return render(request, 'mycollection.html')

def create_project(request):
	return render(request, 'mycreateproject.html')