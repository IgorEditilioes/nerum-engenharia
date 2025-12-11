import os
import django
from decouple import config

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'seu_projeto.settings')
django.setup()

from django.contrib.auth.models import User

username = config('DJANGO_SUPERUSER_USERNAME')
email = config('DJANGO_SUPERUSER_EMAIL')
password = config('DJANGO_SUPERUSER_PASSWORD')

if not User.objects.filter(username=username).exists():
    User.objects.create_superuser(username=username, email=email, password=password)
    print("Superuser criado com sucesso!")
else:
    print("O superuser já existe.")
