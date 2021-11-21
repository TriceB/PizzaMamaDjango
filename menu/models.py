from django.db import models

# Create your models here.
#  define data that will be stored in the database


class Pizza(models.Model):
	name = models.CharField(max_length=200)
	ingredients = models.CharField(max_length=400)
	price = models.FloatField(default=0)
	vegetarian = models.BooleanField(default=False)
	vegan = models.BooleanField(default=False)
	
	def __str__(self):
		return self.name


class Salad(models.Model):
	name = models.CharField(max_length=200)
	ingredients = models.CharField(max_length=400)
	price = models.FloatField(default=0)
	vegetarian = models.BooleanField(default=False)
	vegan = models.BooleanField(default=False)
	
	def __str__(self):
		return self.name


class Pasta(models.Model):
	name = models.CharField(max_length=200)
	ingredients = models.CharField(max_length=400)
	price = models.FloatField(default=0)
	vegetarian = models.BooleanField(default=False)
	vegan = models.BooleanField(default=False)
	
	def __str__(self):
		return self.name
	

class Side(models.Model):
	name = models.CharField(max_length=200)
	price = models.FloatField(default=0)
	vegetarian = models.BooleanField(default=False)
	vegan = models.BooleanField(default=False)
	
	def __str__(self):
		return self.name


class Dessert(models.Model):
	name = models.CharField(max_length=200)
	price = models.FloatField(default=0)
	vegetarian = models.BooleanField(default=False)
	vegan = models.BooleanField(default=False)
	
	def __str__(self):
		return self.name


class Drink(models.Model):
	name = models.CharField(max_length=200)
	price = models.FloatField(default=0)
	
	def __str__(self):
		return self.name
	
	