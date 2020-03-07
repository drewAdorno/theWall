from __future__ import unicode_literals
from django.db import models
import datetime
import re

def isInvalidString(string):

    val=re.search(r'\d', string)
    if val == None:
        return(False)
    return(True)

class UserManager(models.Manager):
    def validator(self, postData):
        errors={}

        now=datetime.datetime.now()
        checkdate = datetime.date(now.year-13, now.month, now.day)
        birthday = datetime.datetime.strptime(postData['birthday'], '%Y-%d-%m').date()
        
        existingEmail=User.objects.filter(email=postData['email'])

        if not postData['first_name']:
            errors['first_name']= "First name is required"
        elif len(postData['first_name'])<2:
            errors['first_name']= "First name has to be at least 2 characters"
        elif isInvalidString(postData['first_name']):
            errors['first_name']= "First name contains invalid characters"
        
        if not postData['last_name']:
            errors['last_name']= "Last name is required"
        elif isInvalidString(postData['last_name']):
            errors['last_name']= "Last name contains invalid characters"
        
        if not postData['email']:
            errors['email']= "Email is required"
        elif '@' not in postData['email'] or '.' not in postData['email']:
            errors['email']= "Email must be valid"
        elif existingEmail:
            errors['email']="Email is already assigned to a current User"
        
        if not postData['password']: 
            errors['password']= "Password is required"
        elif postData['password'] != postData['confirm_password']:
            errors['password']= "Password and Confirm password fields are different"
        
        if not postData['birthday']:
            errors['birthday']= "Birthday is required"
        elif birthday > checkdate:
            errors['birthday']= "You must be at least 13 years old to create an account"
        
        return errors



class User(models.Model):
    first_name=models.TextField(max_length=20)
    last_name=models.TextField(max_length=30)
    email=models.TextField(max_length=30)
    password=models.TextField(max_length=15)
    birthday=models.DateField()
    objects=UserManager()