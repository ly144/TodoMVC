from django.db import models

# Create your models here.
class Todos(models.Model):
	content = models.CharField(max_length=50)
	status = models.IntegerField(default=1)

	def __str__(self):
		return self.content