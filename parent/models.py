from django.db import models

class Parent(models.Model):
	parent_name = models.CharField(max_length=200)

	def __str__(self):
		return self.parent_name

class Child(models.Model):
	parent = models.ForeignKey(Parent, on_delete=models.CASCADE)
	child_name = models.CharField(max_length=200)

	def __str__(self):
		return self.child_name