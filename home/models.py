from django.db import models

# Create your models here.
class ProjectActivity(models.Model):
	value			= models.CharField(max_length=200)
	intensity		= models.IntegerField (default=0)
	
	def __str__(self):
		return self.value
        

class ProjectLanguage(models.Model):
	value 	= models.CharField(max_length=200)
	
	def __str__(self):
		return self.value
        
class Project(models.Model):
	name 		= models.CharField(max_length=200)
	description = models.CharField(max_length=10000)
	url 		= models.URLField(max_length=200)
	languages	= models.ManyToManyField( ProjectLanguage )
	activity	= models.ForeignKey(ProjectActivity, default=0	)
	
	def __str__(self):
		return self.name
        
	
