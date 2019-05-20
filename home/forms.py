from django import forms
from .models import Lead
	
# This model form will allow to display/validate and handle 
# all field from Lead model class
class LeadForm(forms.ModelForm):
	class Meta:
		model = Lead
		fields = ['email','firstname','lastname','phone_number','address','city','state','zip_code','broker','comments',]
