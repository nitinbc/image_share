from django.db import models

# Create your models here.

class MyImages(models.Model):
	title = models.CharField(max_length=65, default="New Pic")
	ifile = models.ImageField(upload_to='pictures/%Y/%m/%d')
	likes = models.IntegerField(default=0,)

	def __str__(self):
		return self.title