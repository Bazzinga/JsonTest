from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=200)
    
    def __unicode__(self):  return self.name

class Story(models.Model):
    name = models.CharField(max_length=200)
    category = models.ForeignKey(Category, related_name='storys') 
    
    def __unicode__(self):  return self.name