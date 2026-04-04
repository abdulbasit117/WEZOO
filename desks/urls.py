import profile
from unittest.mock import patch
from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from .views import change_profile,delete, detail_bron,profile, create_card,cat_by_filter,hot_filter, hov_does, login_view, logout_view, about_as,register_view,cards,contact,index2,day
from .api import CardsViewSet,RegisterViewSet,LoginViewSet,CityViewSet

routers = DefaultRouter()
routers.register('cards',CardsViewSet,basename="cards")
routers.register('register',RegisterViewSet)
routers.register('login',LoginViewSet,basename="login")
routers.register('hot-desks',CityViewSet,basename="hot")



api_urls = [
    path('api/v1/',include(routers.urls))
]



urlpatterns = [
    path('', views.main_page, name='main-page'),
    path('hov/',hov_does,name='hov'),
    path('delete',delete,name='hov'),
    path('bron/<str:title>',detail_bron,name='bron'),
    path('profile/',profile,name='profile'),
    path('edit/',change_profile,name='pro'),
    path("bron/<int:pk>/", detail_bron, name="bron"),
    path('category/<str:category_name>',cat_by_filter,name='hot'),
    path('city/<str:city_name>',hot_filter,name='city'),
    path('about/',about_as,name='about'),
    path('login/',login_view ,name='login'),
    path('logout/', logout_view,name='logout'),
    path('register/', register_view,name='register'),
    path('card/', cards,name='cards'),
    path('contact/',contact,name='contact'),
    path('speak/',index2,name='index2'),
    path('days/',day,name='day'),
    path('create_card/',create_card,name='create_card')
]


urlpatterns+=api_urls


