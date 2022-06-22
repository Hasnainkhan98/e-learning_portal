from django.db import models
from django.contrib.auth.models import User
import os
from django.urls import reverse

def path_and_rename(instance,filename):
	upload_to = 'Images/'
	ext = filename.split('.')[-1]
	#get filename
	if instance.user.username:
		filename = 'User_Profile_Picture/{}.{}'.format(instance.user.username, ext)
	return os.path.join(upload_to,filename)

class UserProfileInfo(models.Model):

	#creating a relationship with user class (not inheriting)
	user= models.OneToOneField(User, on_delete=models.CASCADE)

	#adding additional attributes
	bio = models.CharField(max_length=150, blank=True)
	profile_pic = models.ImageField(upload_to='path_and_rename',verbose_name="Profile Picture", blank=True)

	educator = 'educator'
	student = 'student'
	parent = 'parent'

	user_type = [
		(educator, 'educator'),
		(student, 'student'),
		(parent, 'parent'),
	]

	user_type = models.CharField(max_length=10, choices=user_type, default=student)

	def __str__(self):
		return self.user.username

class Contact(models.Model):
    name = models.CharField(max_length=150)
    email = models.CharField(max_length=150)
    feedback = models.TextField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('index')