
from celery.schedules import timedelta
from celery import shared_task
from django.core.mail import send_mail
from celery import Celery

from time import *
import datetime

# app = Celery()
# @shared_task
# def send_email_to_everyone():     
#     subject = 'Hello, from user,periodic user'
#     message = f'This is a test email sent from Django via Gmail,{datetime.datetime.now()}'
#     from_email = 'ravikumar978069@gmail.com'
#     recipient_list = ['sowndharyams45@gmail.com']  
    
#     send_mail(subject, message, from_email, recipient_list)
   
#     print("Hello from your app!")



