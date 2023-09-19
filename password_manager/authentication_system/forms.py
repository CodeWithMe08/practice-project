from django import forms 
from django.forms import ModelForm
from .models import MyUsers


# Create a venue form
class UserForm(ModelForm):
	class Meta:
		model = MyUsers
		fields = ('first_name','last_name', 'email', 'phone', 'zip_code','address','web', )
		labels = {
			'first_name': '',
			'last_name': '',
			'email': '',
			'phone': '',
			'zip_code': '',
			'address': '',
			'web': '',			
		}
		widgets = {
			'first_name': forms.TextInput(attrs={'id':'firstname','class':'form-control', 'placeholder':'first Name'}),
			'last_name': forms.TextInput(attrs={'id':'lastname','class':'form-control', 'placeholder':'last Name'}),
			'email': forms.EmailInput(attrs={'id':'emailadd','class':'form-control', 'placeholder':'Email'}),
			'phone': forms.TextInput(attrs={'id':'ph','class':'form-control', 'placeholder':'Phone'}),
			'zip_code': forms.TextInput(attrs={'id':'zip','class':'form-control', 'placeholder':'Zip Code'}),
			'address': forms.TextInput(attrs={'id':'locadd','class':'form-control', 'placeholder':'Address'}),
			'web': forms.TextInput(attrs={'id':'webadd','class':'form-control', 'placeholder':'Web Address'}),
			
		}
		