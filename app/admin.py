from django.contrib import admin
from . models import *


# Register your models here.
admin.site.register(Video)
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from . models import *




from import_export.admin import ImportExportModelAdmin

# Here you have to import the User model from your app!
# class BookResource(ImportExportModelAdmin):

#     class Meta:
#         model = User



admin.site.register(CustomUser)