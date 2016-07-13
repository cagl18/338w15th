from django.shortcuts import render, HttpResponseRedirect,Http404
from .forms import LeadForm
from .models import Lead
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.

def get_ip(request):
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
	content = {}
	template= "thanks.html"
	return render(request, template, content)

def home(request):
	form = LeadForm(request.POST or None)

	if form.is_valid():
		# do not save it yet
		new_lead = form.save(commit=False)
		#used in case we would like to redirect the user to another page if email already exist.
		email = form.cleaned_data['email']
		new_lead.ip_address = get_ip(request)
		new_lead.save()

		from_email = settings.DEFAULT_FROM_EMAIL
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
			send_mail(subject, message, from_email, ['cgonzalez@townresidential.com'],
				fail_silently=False)
		except:
			pass
		return HttpResponseRedirect("/thanks")

		# return render(request, "yourapp/email.html", {'form': form})
	# content = {"form":form,"image":'home.png'}
	content = {"form":form}
	template= "home.html"
	return render(request, template, content)

# def thanks(request):
#     return HttpResponse('Thank you for your message.')



# 	    contact_name = request.POST.get(
#                 'contact_name'
#             , '')
#             contact_email = request.POST.get(
#                 'contact_email'
#             , '')
#             form_content = request.POST.get('content', '')

#             # Email the profile with the 
#             # contact information
#             template = 
#                 get_template('contact_template.txt')
#             context = Context({
#                 'contact_name': contact_name,
#                 'contact_email': contact_email,
#                 'form_content': form_content,
#             })
#             content = template.render(context)

#             email = EmailMessage(
#                 "New contact form submission",
#                 content,
#                 "Your website" +'',
#                 ['youremail@gmail.com'],
#                 headers = {'Reply-To': contact_email }
#             )
#             email.send()
#             return redirect('contact')

# 	    #print all "friends" that joined as a result of main sharer email
# 	    # print(Join.objects.filter(friend=obj).count())
# 	    # print(obj.referral.all().count())

# 	    #redirect here
# 	    return HttpResponseRedirect("/thanks")

# 	content = {"form":form,"image":'home.png'}
# 	template= "home.html"
# 	return render(request, template, content)










# 	if request.method == 'POST':
#         form = form_class(data=request.POST)

#         if form.is_valid():
#             contact_name = request.POST.get(
#                 'contact_name'
#             , '')
#             contact_email = request.POST.get(
#                 'contact_email'
#             , '')
#             form_content = request.POST.get('content', '')

#             # Email the profile with the 
#             # contact information
#             template = 
#                 get_template('contact_template.txt')
#             context = Context({
#                 'contact_name': contact_name,
#                 'contact_email': contact_email,
#                 'form_content': form_content,
#             })
#             content = template.render(context)

#             email = EmailMessage(
#                 "New contact form submission",
#                 content,
#                 "Your website" +'',
#                 ['youremail@gmail.com'],
#                 headers = {'Reply-To': contact_email }
#             )
#             email.send()
#             return redirect('contact')

#     return render(request, 'contact.html', {
#         'form': form_class,
#     })