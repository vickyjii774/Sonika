import os
from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand
class Command(BaseCommand):
 help='Create the first deployment admin from environment variables if it does not exist.'
 def handle(self,*args,**kwargs):
  username=os.getenv('DJANGO_SUPERUSER_USERNAME','').strip(); email=os.getenv('DJANGO_SUPERUSER_EMAIL','').strip(); password=os.getenv('DJANGO_SUPERUSER_PASSWORD','')
  if not (username and email and password): self.stdout.write('Deployment admin variables not set; skipping.'); return
  User=get_user_model()
  if User.objects.filter(username=username).exists(): self.stdout.write('Deployment admin already exists; leaving it unchanged.'); return
  User.objects.create_superuser(username=username,email=email,password=password)
  self.stdout.write(self.style.SUCCESS('Deployment admin created.'))
