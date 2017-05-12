from __future__ import unicode_literals
from datetime import datetime
from django.db import models

# Create your models here.
class  Todo(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_at = models.DateTimeField(default=datetime.now,blank=True)

    def __str__(self): #django adminde olstrdugmuz todolarn  tdo object olarak titlelaryla goruntulernmelrni saglayacak.
        return self.title