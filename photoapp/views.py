from django.shortcuts import render,HttpResponse, HttpResponseRedirect, redirect, reverse

from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.decorators import login_required
from .forms import UserForm,CreatePostForm,UpdatePostForm,CreateCommentForm, UpdateProfileForm,searchuform
from django.contrib.auth.models import User
from .models import Profile,Post, Comment, Likes
from django.core.files.storage import FileSystemStorage
from django.utils import timezone
from django.views.generic import ListView



def index(request):
	return render(request,'photoapp/home.html')


def signup(request):
	if request.method=='POST':
		form=UserForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			raw_password=form.cleaned_data.get('password1')
			return redirect('login')
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
				return redirect('/home')
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
			
			return redirect('/home')
	else:
		form=CreatePostForm()
	
    
	return render(request,'photoapp/postenter.html',{'form':form})

def update_profile(request):
	if request.method=='POST':
		form=UpdateProfileForm(request.POST,request.FILES, instance=request.user.profile)
		if form.is_valid():
			form.save()

			return redirect('/home')

	else:
		form=UpdateProfileForm()

	return render(request,'photoapp/update_profile.html',{'form':form})


def home(request):
	users=User.objects.all()
	print(users)
	
	pk=request.user
	
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
	comments=Comment.objects.filter(post=posts).order_by('-date')
	liked=Likes.objects.filter(post=posts)
	print(liked.count())
	l=liked.count()
	co=[]
	lo=[]
	for i in liked:
		lo.append(i)


	for i in comments:
		#print(i.text)l
		#print(type(i))
		co.append(i)
	#print(co)
	print(co)
	#print(posts.author)
	#print(request.user)
	if posts.author==request.user:
		return render(request,'photoapp/viewpost2.html',{'posts':posts,'co':co, 'l':l, 'user':request.user, 'likes':lo})
	else:
		return render(request,'photoapp/viewpost.html',{'posts':posts,'co':co, 'l':l, 'user':request.user, 'likes':lo})

def update_post(request,key):
	posts=Post.objects.get(id=key)
	if request.method=='POST':
		form=UpdatePostForm(request.POST)
		if form.is_valid():
			#posts=form.save(commit=False)
			#posts.author=request.user
			posts.image=posts.image
			posts.caption=form.cleaned_data['caption']
			posts.location=form.cleaned_data['location']
			posts.date_posted=timezone.now()
			posts.save()

			return redirect('/home')
	else:
		form=UpdatePostForm()

	return render(request,'photoapp/update_post.html',{'form':form})

def create_comment(request,key):
	posts=Post.objects.get(id=key)
	comments=Comment.objects.filter(post=posts)
	comment_list=[]
	print(posts)
	print(comments)
	if request.method=='POST':
		form=CreateCommentForm(request.POST)
		if form.is_valid():
			p=form.save(commit=False)
			p.author=request.user
			p.post=posts
			p.save()
			next = request.POST.get('next',None)
			#return HttpResponseRedirect(next)
			#return redirect('/home/key/')
			return redirect('/home/%s' % key )
	else:
		form=CreateCommentForm()
	for i in comments:
		print(i)

	return render(request,'photoapp/create_comment.html',{'form':form})
def like_post(request,key):
	posts=Post.objects.get(id=key)
	liked=Likes()
	liked.post=posts
	liked.users=request.user
	liked.save()
	return redirect('/home/%s' % key )
	


def searchuser(request):
	if request.method=='POST':
		print('2')
		t=0
		form=searchuform(request.POST)
		usn=User.objects.all()
		print(len(usn))
		#f=form.cleaned_data['username']
		print(form)
		for i in usn:
			#if i.username==form.username:
				print(i.username)
		
		
		if form.is_valid():
			print('17')
			print(form)
			f=form.cleaned_data['username']
			print(f)
			for k in usn:
				if k.username==f:
					print(k.last_name)
					t=1
					break
			if t:	
				return render(request,'photoapp\show.html',{'k':k})
			else:
				return render(request,'photoapp\invalidsearch.html')
		#	print('1')
		#	j=form.save(commit=False)
		#	usinst=User.objects.get(username=j.username)
		#	print(usinst)
		#	return render(request,'show.html',{'usinst':usinst})
		#else:
		#	form=searchuform()
	else:
		form=searchuform()
	return render(request,'photoapp\search.html',{'form':form})






