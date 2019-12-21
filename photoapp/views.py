from django.shortcuts import render,HttpResponse, HttpResponseRedirect, redirect

from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.decorators import login_required
from .forms import UserForm,CreatePostForm,UpdatePostForm
from django.contrib.auth.models import User
from .models import Profile,Post
from django.core.files.storage import FileSystemStorage
from django.utils import timezone


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
			p=form.save(commit=False)
			p.author=request.user
			p.date_posted=timezone.now()
			p.save()
			#form.save()
			
			return redirect('/')
	else:
		form=CreatePostForm()
	
    
	return render(request,'photoapp/postenter.html',{'form':form})

def home(request):
	users=User.objects.all()
	print(users)
	#profiles=Profile.objects.post.order_by('date_posted')
	#print(profiles)
	pk=request.user
	#rint(pk)
	following=[]
	posts=Post.objects.order_by("-date_posted")
	for i in users:
		#users=User.objects.get(id=user_id)
		#print(i.pk)
		#print(i)
		#print(i.profile.bio)
		#print(i.profile.caption)
		#print(i.profile.followers.all())
		if pk in i.profile.followers.all():

			following.append(i.pk)
	#print(following)
	post_list=posts
	#print(post_list)
	return render(request,'photoapp/postlist.html',{'posts':post_list})

def confirm_delete(request,key):
	posts=Post.objects.get(id=key)
	return render(request,'photoapp/confirm_delete.html',{'posts':posts})

def delete_post(request,key):
	posts=Post.objects.get(id=key)
	posts.delete()
	return redirect('/home')


def view_post(request,key):
	posts=Post.objects.get(id=key)
	print(posts.author)
	print(request.user)
	if posts.author==request.user:
		return render(request,'photoapp/viewpost2.html',{'posts':posts})
	else:
		return render(request,'photoapp/viewpost.html',{'posts':posts})

def update_post(request,key):
	posts=Post.objects.get(id=key)
	if request.method=='POST':
		form=UpdatePostForm(request.POST)
		if form.is_valid():
			#posts=form.save(commit=False)
			#posts.author=request.user
			#posts.image=posts.image
			posts.caption=form.cleaned_data['caption']
			posts.location=form.cleaned_data['location']
			posts.date_posted=timezone.now()
			posts.save()

			return redirect('/home')
	else:
		form=UpdatePostForm()

	return render(request,'photoapp/update_post.html',{'form':form})






