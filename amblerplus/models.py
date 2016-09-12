from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
import os

# Create your models here.

def content_file_name(instance, filename):
    return os.path.join(instance.job, filename)

class Job(models.Model):
    job = models.CharField(max_length=40, primary_key=True)
    creation_date = models.DateTimeField(auto_now_add=True)  # adds timestamp at creation moment
    submit_date = models.DateTimeField(null=True, blank=True)
    email = models.EmailField(max_length=254, null=True, blank=True)  # default is NULL
    description = models.CharField(max_length=60, null=True, blank=True)
   
    def __unicode__(self):
        return str(self.job)

    def getDate(self):
        return self.creation_date.strftime('%Y-%m-%d %H:%M:%S')


class Result(models.Model):
    id = models.AutoField(primary_key=True)
    job = models.ForeignKey(Job)
        
    def __unicode__(self):
        return str(self.job)

