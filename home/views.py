from django.shortcuts import render, HttpResponseRedirect,Http404
from .forms import LeadForm
from .models import Lead
from django.core.mail import EmailMessage
from django.conf import settings

def get_ip(request):
	 #this function will try to get user ip address from the request. 
	try:
		x_forward = request.META.get("HTTP_X_FORWARDED_HOST")
		if x_forward:
			ip = x_forward.split(",")[0]
		else:
			ip = request.META.get("REMOTE_ADDR")
	except:
		ip = ""
	return ip


def thanks(request):
	context = {}
	template= "thanks.html"
	return render(request, template, context)

def home(request):
	form = LeadForm(request.POST or None)

	if form.is_valid(): 
		new_lead = form.save(commit=False) # do not save form data yet
		#used in case we would like to redirect the user to another page if email already exist.
		new_lead.ip_address = get_ip(request)
		new_lead.save()

		# preparing email content
		email = form.cleaned_data['email']
		from_email = settings.DEFAULT_FROM_EMAIL
		# receipts = ['prince@townresidential.com','jperkal@townresidential.com','ktruglio@townresidential.com']
		web_admin_email = ['cgonzalez@townresidential.com']
		receipts = web_admin_email
		subject = 'New Lead:338 West 15th'
		firstname = form.cleaned_data['firstname']
		lastname = form.cleaned_data['lastname']
		phone_number = form.cleaned_data['phone_number']
		email = form.cleaned_data['email']
		address = form.cleaned_data['address']
		city = form.cleaned_data['city']
		state = form.cleaned_data['state']
		zip_code = form.cleaned_data['zip_code']
		if form.cleaned_data['broker']:
			broker = 'Yes'
		else:
			broker = 'No'
		comments = form.cleaned_data['comments']
		message = 'Great News, You got a new lead! \n\nName: %s %s \nPhone: %s \nEmail: %s \nAddress: %s %s %s %s \nBroker: %s \nComment / Questions?: %s' \
		%(firstname,lastname,phone_number,email,address,city,state,zip_code,broker,comments)

		try:
			email = EmailMessage(
				subject,
				message,
				from_email,
				receipts,
				web_admin_email,
				# reply_to=['another@example.com'],
				# headers={'Message-ID': 'foo'},
			)
			email.send()
			return HttpResponseRedirect("/thanks")
		except:
			pass
			# report issue to developer
			subject = "Error email send failed" + subject
			message = "Error occured while trying to send email to website owner.\n Original message:" + message
			email = EmailMessage(
				subject,
				message,
				web_admin_email,
				web_admin_email,
			)
			email.send()

	content = {"form":form}
	template= "home.html"
	return render(request, template, content)





