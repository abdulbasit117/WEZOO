from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.conf import settings


class Booking(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="bookings")
    card = models.ForeignKey("Cards", on_delete=models.CASCADE, related_name="bookings")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} -> {self.card}"





class CustomUser(AbstractUser):
    phone = models.CharField(
        _('Телефон'),
        max_length=15,
        blank=True,
        null=True
    )
    images = models.ImageField(
        verbose_name='Фото профиля',
        blank=True,
        upload_to='users/',
        null=True
    )

    is_married = models.BooleanField(
        _('Женат / Замужем'),
        default=False
    )

    age = models.PositiveSmallIntegerField(
        _('Возраст'),
        blank=True,
        null=True
    )

    def __str__(self):
        return self.username
    



class Category(models.Model):
    name = models.CharField(
        verbose_name="Имя категория",
        blank=True,
        null=True,
    )
    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name
    




class City(models.Model):
    foto_city = models.ImageField(
        verbose_name='картинка города',
        upload_to='cities/', 
    )

    name_city = models.TextField(
     verbose_name='названия города'   
    )
    category = models.ForeignKey(
        'Category',
        on_delete=models.CASCADE,
        related_name="hot",
        blank=True,
        null=True,
    )
    def __str__(self):
        return self.name_city
    


class Cards(models.Model):
    title = models.TextField(
        blank=True,
        null=True,
        verbose_name='Названия'
    )
    image = models.ImageField(
        blank=False,
        null=False,
        upload_to='cards/',
        verbose_name='Картинка карточки'
    )
    author = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name="cards",
        blank=True,
        null=True
    )
    address = models.CharField(
        verbose_name='Адрес точки',
        max_length=100,
        null=True,
        blank=True
    )
    
    feedback = models.FloatField(
        blank=True,
        null=True,
        verbose_name='Оценка'
    )

    description = models.TextField(
        verbose_name='Описания',
        max_length=350,
        blank=True,
        null=True
    )
    price = models.IntegerField(
        verbose_name='Начальная цена',
        null=True,
        blank=True
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="category",
        blank=True,
        null=True
    )
    city = models.ForeignKey(
        City,
        on_delete=models.CASCADE,
        related_name="city",
        blank=True,
        null=True
    )
    

    def __str__(self):
        return self.title


