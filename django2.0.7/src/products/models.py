from django.db import models

# Create your models here.
class Product(models.Model):
	Title 		= models.CharField(max_length=120) # max_length is required
	Description	= models.TextField(blank=True, null=True) # blank -> field
	Price		= models.DecimalField(decimal_places=2, max_digits=10000)
	Summary		= models.TextField()
	Featured	= models.BooleanField(default=True) # null=True