from django.db import models

class Content(models.Model):
	id = models.AutoField(primary_key=True)
	publish = models.BooleanField(default=False)
	title = models.CharField(max_length=200)
	content = models.TextField(blank=True)
	background = models.ImageField(blank=True)
	public	= models.BooleanField(default=False)

	class Meta:
		verbose_name = 'content'
		verbose_name_plural = 'content'

	def __str__(self):
		return str(self.title)