from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth import get_user_model
import threading
import traceback

User = get_user_model()

def _send_welcome(email, username):
    try:
        send_mail(
            "Добро пожаловать!",
            f"Здравствуйте, {username}! Спасибо за регистрацию на нашем сайте.",
            settings.EMAIL_HOST_USER,
            [email],
            fail_silently=False,
        )
    except Exception as e:
        print("EMAIL ERROR:", repr(e))
        traceback.print_exc()

@receiver(post_save, sender=User)
def send_welcome_email(sender, instance, created, **kwargs):
    if not created or not instance.email:
        return

    threading.Thread(
        target=_send_welcome,
        args=(instance.email, instance.username),
        daemon=True
    ).start()

