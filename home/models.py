from django.db import models
from django.core.validators import RegexValidator

# Create your models here.
class Lead(models.Model):
	firstname = models.CharField(max_length =120)
	lastname = models.CharField(max_length =120)
	phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
	phone_number = models.CharField(max_length =16, validators=[phone_regex], blank=True, null=True) # validators should be a list
	email = models.EmailField()
	address = models.CharField(max_length =120, blank=True, null=True)
	city = models.CharField(max_length =60, blank=True, null=True)
	state = models.CharField(max_length =60, blank=True, null=True)
	zip_code = models.CharField(max_length =5, blank=True, null=True)
	broker = models.BooleanField()
	comments = models.TextField(blank=True, null=True)
	ip_address = models.CharField(max_length=120, default = 'NA')
	timestamp = models.DateTimeField(auto_now_add = True, auto_now = False)

	# this str function needs to return a string
	def __str__(self):
		return self.email

		# label='Are You a broker?'
		# label='Comments or Questions?', 