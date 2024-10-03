from django.contrib import admin

# Register your models here.
from .models import *
admin.site.register(Profile) # we want to access the Profile model from the admin