##Model

from django.db import models
 
class to_do(models.Model):
         
    nombre = models.CharField(max_length=100, unique=True) 
    tiempo = models.DateTimeField() 
 
    def __unicode__(self):
        return self.name


##Templates
 INSTALLED_APPS = (
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'todo.core',
    )
##Admin
