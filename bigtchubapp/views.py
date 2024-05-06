from django.shortcuts import render, redirect

from django.core.mail import BadHeaderError, send_mail

from django.http import HttpResponse

from django.contrib import messages

from .forms import *


# Create your views here.

def home(request):
	return render(request, 'bigtchubapp/home.html')

def about(request):
	return render(request, 'bigtchubapp/about.html')

def contact(request):
	if request.method == 'GET':
		form= ContactForm()
	else:
		form = ContactForm(request.POST or None)
		if form.is_valid():
			name= form.cleaned_data['name']
			email= form.cleaned_data['email']
			message= form.cleaned_data['message']
			print(name)
		try:
			send_mail(name, "User with name {} and email {} has sent a message saying: {}".format(name, email, message),email, ['daniel@bigtchub.com'])
			print('Message Sent')
		except:
			print('Message not sent')
			messages.error(request, 'Message Not sent, Try again later.')
		messages.success(request, 'Your message has been sent successfully')
	context={'form':form}
	return render(request, 'bigtchubapp/contact.html', context)

def realtorscanonwebsite(request):
	return render(request, 'bigtchubapp/webfeatures.html')

def realtorscanon(request):
	return render(request, 'bigtchubapp/realtorscanon.html')

def plutopay(request):
	return render(request, 'bigtchubapp/plutopay.html')

def fancreo(request):
	return render(request, 'bigtchubapp/fancreo.html')

def infringobuy(request):
	return render(request, 'bigtchubapp/infringobuy.html')

def signup(request):
	return render(request, 'bigtchubapp/signup.html')

