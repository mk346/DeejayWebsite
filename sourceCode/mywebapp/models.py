from django.db import models
from embed_video.fields import EmbedVideoField
from django.core.validators import validate_slug, validate_email
from .validators import validate_domainonly_email



# Create your models here.
class FilesAdmin(models.Model):
	genre = models.CharField(max_length=100)
	title= models.CharField(max_length=100)
	adminupload = models.FileField(upload_to='media')
	added_date = models.DateTimeField(auto_now_add=True)


	def __str__(self):
		return self.title

	class Meta:
		ordering = ['-added_date']


class Item(models.Model):
	title = models.CharField(max_length=100)
	added_date = models.DateTimeField(auto_now_add=True)
	thumbnail = models.ImageField(upload_to='media/thumbnail' ,null=True, blank=True)
	video_url = EmbedVideoField()

	def __str__(self):
		return self.title

	class Meta:
		ordering = ['-added_date']


class Popular(models.Model):
	name = models.CharField(max_length=100)
	video_image = models.ImageField(upload_to='media/thumbnail' ,null=True, blank=True)
	pop_video_url = EmbedVideoField()

	def __str__(self):
		return self.name

	
	class Meta:
		ordering = ['-name']


class Contact(models.Model):
	name = models.CharField(max_length=100)
	email= models.EmailField(validators=[validate_domainonly_email])
	subject= models.CharField(max_length=500)
	message= models.TextField()

	def __str__(self):
		return self.name


class Bookings(models.Model):
	name = models.CharField(max_length=100)
	email = models.EmailField()
	phone = models.CharField(max_length=100)
	ev_location = models.CharField(max_length=100)
	ev_Date = models.DateField()
	ev_Time = models.TimeField()

	def __str__(self):
		return self.name


class Updates(models.Model):
	Name = models.CharField(max_length=100 ,blank=True)
	Description = models.TextField(blank=True)
	update_image = models.ImageField(upload_to='media/thumbnail' ,blank=True)
	update_video = EmbedVideoField( blank=True)

	def __str__(self):
		return self.Name

class Details(models.Model):
	description = models.TextField()
	det_image = models.ImageField()

	def __str__(self):
		return self.description


        
    


   

    
    	


