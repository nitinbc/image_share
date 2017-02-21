from django import forms
from .models import MyImages



AVAILABLE_FILTERS = (
	(1, 'None'),
	(2, "Filter 1"),
	(3, "FIlter 2")
	)
class iform(forms.ModelForm):

	ifilter = forms.ChoiceField(choices=AVAILABLE_FILTERS, required=True)
	class Meta:
		model=MyImages
		fields = ['ifile', 'title' ]

