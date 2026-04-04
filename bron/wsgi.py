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
    
    
    
    from django.contrib.auth import get_user_model

User = get_user_model()

try:
    if not User.objects.filter(username="admin").exists():
        User.objects.create_superuser(
            username="admin",
            email="admin@gmail.com",
            password="admin123"
        )
        print("Superuser created")
except Exception as e:
    print("Superuser error:", e)