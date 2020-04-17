from django.db import models

class Account(models.Model):
	username = models.CharField(max_length = 50)
	password = models.CharField(max_length = 400)

	class Meta:
		db_table = 'accounts'
