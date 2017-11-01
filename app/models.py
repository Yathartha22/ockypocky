from django.db import models

class Category(models.Model):
	category = models.CharField(max_length=200)
	parent = models.ForeignKey('self', blank=True, null=True, related_name='children')

	class Meta:
		unique_together = ('parent' , 'category')
		verbose_name_plural = "Categories"

	def __str__(self):
		return self.category

class SubCategory(models.Model):
	subcategory = models.CharField(max_length=200)
	category = models.ForeignKey('Category', null=True, blank=True)
	parent = models.ForeignKey('self', blank=True, null=True, related_name='subchilren')

	class Meta:
		unique_together = ('parent' , 'subcategory')
		verbose_name_plural = "Sub Categories"

	def __str__(self):
		return self.subcategory

class Product(models.Model):
	name = models.CharField(max_length=200)
	category = models.ForeignKey('Category', null=True, blank=True)
	subcategory = models.ForeignKey('SubCategory', null=True, blank=True)

	def __str__(self):
		return self.name
