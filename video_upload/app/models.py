from django.db import models

# Create your models here.

from django.db import models


from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone
# class CustomUserManager(BaseUserManager):
#     def create_user(self, username, email, phone=None, image=None, password=None, **extra_fields):
#         if not email:
#             raise ValueError('The Email field must be set')
#         email = self.normalize_email(email)
#         user = self.model(username=username, email=email, phone=phone, image=image, **extra_fields)
#         user.set_password(password)
#         user.save(using=self._db)
#         return user

#     def create_superuser(self, username, email, password=None, **extra_fields):
#         extra_fields.setdefault('is_staff', True)
#         extra_fields.setdefault('is_superuser', True)
#         return self.create_user(username, email, password=password, **extra_fields)

class CustomUser(AbstractUser):
    phone = models.CharField(max_length=15, blank=True, null=True)
    image = models.ImageField(upload_to='user_images/', blank=True, null=True)

    # objects = CustomUserManager()

class Video(models.Model):
    title = models.CharField(max_length=100)
    video_file = models.FileField(upload_to='videos/')
    user=models.ForeignKey(CustomUser,on_delete=models.CASCADE,null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
