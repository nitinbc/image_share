from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext
from django.core.urlresolvers import reverse

from .forms import ContactForm
from .models import Contact_db
# Create your views here.

def contact(request):

	if request.method == 'POST':
		form = ContactForm()
		if form.is_valid():
			contacted = Contact_db()
			contacted.name = form.cleaned_data.get('name')
			contacted.email = form.cleaned_data.get('email')
			contacted.content = form.cleaned_data.get('content')
			contented.save()
			return HttpResponse('Saved')
	else:
		return HttpResponse('Sorry, we couldn\'t catch that' )	
	

