from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django.dispatch import receiver
from django.db.models.signals import post_save


class Profile(models.Model):
	user=models.OneToOneField(User,on_delete=models.CASCADE)
	bio=models.TextField(max_length=500, blank=True)
	birthdate=models.DateField(null=True,blank=True)
	image = models.ImageField(default='default.jpg', upload_to='profile_pics')
	followers=models.ManyToManyField(User, blank=True, related_name='user_followers')

	def __str__(self):
		return str(self.user)

@receiver(post_save,sender=User)

def create_user_profile(sender, instance, created, **kwargs):
	if created:
		Profile.objects.create(user=instance)
@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


class Post(models.Model):
	caption=models.CharField(max_length=100)
	image=models.ImageField(upload_to='images/')
	location=models.TextField()
	date_posted = models.DateTimeField(default=timezone.now)
	author=models.ForeignKey(User,on_delete=models.CASCADE)
	likes = models.ManyToManyField(User, blank=True, related_name='post_likes')

	def __str__(self):
		return self.caption


class Comment(models.Model):
	post = models.ForeignKey('photoapp.Post', on_delete=models.CASCADE, related_name='comments')
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	text=models.TextField(max_length=200)
	date=models.DateTimeField(default=timezone.now())

	def __str__(self):
		return self.text
