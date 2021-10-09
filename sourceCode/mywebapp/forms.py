from django import forms
from .models import FilesAdmin,Bookings
from django.forms import ModelForm

class myForm(forms.ModelForm):
	class Meta:
		model = FilesAdmin
		fields = {'genre', 'title', 'adminupload' }

		labels = {
		    'genre': '',
		    'title': '',
		}

		widgets = {
		    'genre':forms.TextInput(attrs={'class':'form-control', 'Placeholder':'Mix Genre' }),
		    'title':forms.TextInput(attrs={'class':'form-control', 'Placeholder':'Mix Title' }),
		    




		}


class bookingForm(ModelForm):
	class Meta:
		model = Bookings
		fields = '__all__'
		labels = {
		    'name':'Your Name','class':'form-label',
		    'email':'Your Email','class':'form-label',
		    'phone':'Your Phone Number','class':'form-label',
		    'ev_location':'Event Location eg; home address,club location','class':'form-label',
		    'ev_Date':'Event Date','class':'form-label',
		    'ev_Time':'Event Time','class':'form-label',
		}

		widgets = {
		    'name':forms.TextInput(attrs={'class':'form-control', 'Placeholder':'your name',}),
		    'email':forms.EmailInput(attrs={'class':'form-control', 'Placeholder':'your email','type':'email'}),
		    'phone':forms.TextInput(attrs={'class':'form-control', 'Placeholder':'your phone number',}),
		    'ev_location':forms.TextInput(attrs={'class':'form-control', 'Placeholder':'address',}),
		    'ev_Date':forms.TextInput(attrs={'class':'form-control', 'Placeholder':'enter the event date','type':'date'}),
		    'ev_Time':forms.TextInput(attrs={'class':'form-control', 'Placeholder':'your name','type':'time'}),






		}

