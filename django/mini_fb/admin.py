from django.contrib import admin

# Register your models here.
from .models import *
admin.site.register(Profile) # we want to access the Profile model from the admin
admin.site.register(StatusMessage) # we want to access the StatusMessage model from the admin
admin.site.register(Image) # we want to access the Image model from the admin
admin.site.register(Friend) # we want to access the Friend model from the admin