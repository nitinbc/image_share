from django.shortcuts import render
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse

from .models import MyImages
from .forms import iform
from contact.forms import ContactForm

from FilterSite.decorators import ajax_required

# Create your views here.

def ilist(request):
	if request.method == 'POST':
		form = iform(request.POST, request.FILES)
		if form.is_valid():
			filter_selected = form.cleaned_data.get('ifilter')
			newpic = MyImages(title= form.cleaned_data.get('title'),ifile=request.FILES['ifile'])
			newpic.save()

			return HttpResponseRedirect(reverse('list'))

	else:
		form = iform()
		contact_form = ContactForm()

	images = MyImages.objects.all()
	return render(request, 'list.html', {'images':images,
											'form':form,
											'contact_form':contact_form})


@ajax_required
def like(request):
	pic_id = request.POST['pic_id']
	image = MyImages.objects.get(id=pic_id)
	image.likes += 1
	likes = image.likes
	return HttpResponse (likes)
