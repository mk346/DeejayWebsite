from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .models import FilesAdmin, Item, Popular, Contact,Bookings,Updates,Details
from django.views.generic import TemplateView
from .forms import myForm,bookingForm
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string

# Create your views here.
def home(request):
	pop_videos = Popular.objects.all()
	updates = Updates.objects.all()
	detail = Details.objects.all()
	return render(request,'mywebapp/index.html', {'pop_videos':pop_videos,'updates':updates,'detail':detail})

def services(request):
	form = bookingForm()
	if request.method == "POST":
		form = bookingForm(request.POST)
		if form.is_valid():
			form.save()
			Name = form.cleaned_data['name']
			Email = form.cleaned_data['email']
			Phone = form.cleaned_data['phone']
			ev_location = form.cleaned_data['ev_location']
			ev_Date = form.cleaned_data['ev_Date']
			ev_Time = form.cleaned_data['ev_Time']

			data = {
			    'Name': Name,
			    'email': Email,
			    'location':ev_location,
			    'phone': Phone,
			    'Date' : ev_Date,
			    'Time' : ev_Time,
			}

			Message = '''
			Name: {}
			Phone Number: {}
			Location: {}
			Event Date: {}
			Event Time: {}
			Sender Email: {}
			'''.format(data['Name'],data['phone'],data['location'],data['Date'],data['Time'],data['email'])
			send_mail(data['email'],Message,'',['kinyuacaleb554@gmail.com'])

			return render(request,'mywebapp/services.html',{'Name':Name})
	else:
		return render(request,'mywebapp/services.html',{'form':form})

			
	


def about(request):
	return render(request,'mywebapp/about.html')


def contact(request):
	if request.method == "POST":
		contact = Contact()
		name = request.POST['name']
		from_email = request.POST['email']
		subject = request.POST['subject']
		message = request.POST['message']
		contact.name = name
		contact.email = from_email
		contact.subject = subject
		contact.message = message
		contact.save()

		data = {
		    'name': name,
		    'from_email': from_email,
		    'subject': subject,
		    'message': message,

		} 
		message = '''
		Name: {}
		New message: {}

		From: {}
		'''.format(data['name'],data['message'],data['from_email'])


		send_mail(data['subject'],message,'',['kinyuacaleb554@gmail.com']) 

		return render(request,'mywebapp/contact.html',{'name':name})



	else:
		return render(request,'mywebapp/contact.html',{})




	

def upload(request):
	if request.method == 'POST':
		#uploaded_file = request.FILES['adminupload']
		#print(uploaded_file.size)
		form = myForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return redirect('mymixes')
	else:
		form = myForm()
	return render(request, 'mywebapp/upload.html', {'form':form})		


def mixes(request):
	mixes = FilesAdmin.objects.all()
	#print(uploaded_file.size)
	return render(request,'mywebapp/mixes.html', {'mixes':mixes})


def video(request):
	videos = Item.objects.all()
	return render(request,'mywebapp/video.html',{'videos':videos})




