from django.db import models

class Parent(models.Model):
	parent_name = models.CharField(max_length=200)
	child_id = models.CharField(max_length=200)

	def __str__(self):
		return self.parent_name