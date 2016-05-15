from django import forms
from .models import Lead

# class LeadForm(forms.Form):
# 	email = forms.EmailField(required = True)
# 	firstname = forms.CharField(required = True)
# 	lastname = forms.CharField(required = True)
#     phone_number = forms.CharField(required = False)
# 	address = forms.CharField(required = False)
# 	city = forms.CharField(required = False)
# 	state = forms.CharField(required = False)
# 	zip_code = forms.CharField(required = False)
# 	broker = forms.BooleanField(required = False)
# 	comments = forms.TextField(required = False)
	
# This model form will allow to display/validate and handle 
# all field from Join model class
class LeadForm(forms.ModelForm):
	class Meta:
		model = Lead
		fields = ['email','firstname','lastname','phone_number','address','city','state','zip_code','broker','comments',]
