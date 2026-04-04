import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bron.settings')

application = get_wsgi_application()

# 🔥 ДОБАВЬ ЭТО НИЖЕ
from django.core.management import call_command

try:
    call_command('migrate', interactive=False)
except Exception as e:
    print("Migration error:", e)