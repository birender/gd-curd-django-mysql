from django.db import models

class StudentModel(models.Model):
	name = models.CharField(max_length=100)
	age = models.IntegerField()
	section = models.CharField(max_length=20)

	def __str__(self):
		return self.name

	def getUpdateUrl(self):
		return f"update/{self.id}/"

	def getDeleteUrl(self):
		return f"delete/{self.id}/"