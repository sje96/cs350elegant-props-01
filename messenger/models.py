# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class message(models.Model):
	subject = models.CharField(max_length=256)
	message = models.TextField()
	date = models.DateField(auto_now=True)
	email = models.EmailField(max_length=256)