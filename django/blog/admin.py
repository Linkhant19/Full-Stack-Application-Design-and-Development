from django.contrib import admin

# Register your models here.
from .models import *
admin.site.register(Article) # we want to access the Article model from the admin
admin.site.register(Comment)