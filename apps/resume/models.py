# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import validate_email

# Create your models here.
class messageVal(models.Manager):
    def textValidation(self, name, email, text):
        errors =[]
        if len(name) <= 3:
            errors.append("Use full name please")
        elif name.isalpha() == False:
            errors.append("Thats not a name")
        if email != "":
            try:
                validate_email(email)
            except ValidationError as e:
                errors.append("Please use valid email")
        if len(text) <= 10:
            errors.append("10 Characters min.")
        if len(text) > 1000:
            errors.append("1000 Character max.")
        else:
            return errors            

class Texts(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    text = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    object = messageVal()
