from django.db import models

# Create your models here.

class Contact_db(models.Model):
	name = models.CharField(max_length=75)
	email = models.EmailField(max_length=80)
	content = models.TextField()

	def __str__(self):
		return self.email