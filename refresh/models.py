# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

# Create your models here.

class Refresh(models.Model):
    datetime =  models.DateTimeField()
    url = models.CharField(max_length=1000)
    ip = models.CharField(max_length=1000)
