from django.shortcuts import render,HttpResponse, HttpResponseRedirect, redirect

from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.decorators import login_required
from .forms import UserForm,CreatePostForm
from django.contrib.auth.models import User
from .models import Profile,Post
from django.core.files.storage import FileSystemStorage



def index(request):
	return render(request,'photoapp/home.html')


def signup(request):
	if request.method=='POST':
		form=UserForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/')
	else:
		form=UserForm()
	args={'form': form}
	return render(request,'photoapp/signup.html',args)


def login_view(request):
	message='Log In'
	if request.method=='POST':
		_username=request.POST['username']
		_password=request.POST['password']
		user=authenticate(username=_username,password=_password)
		if user is not None:
			if user.is_active:
				login(request,user)
				return redirect('/')
			else:
				message='Not Activated'
		else:
			message='Invalid Login'
	context={'message':message}
	return render(request,'photoapp/login.html',context)

@login_required
def logout_view(request):
	logout(request)
	return HttpResponseRedirect('/')

@login_required
def create_post(request):
	if request.method=='POST':
		form=CreatePostForm(request.POST,request.FILES)
		if form.is_valid():
			form.save()
			
			return redirect('/')
	else:
		form=CreatePostForm()
	
    
	return render(request,'photoapp/postenter.html',{'form':form})


