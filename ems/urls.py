from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^check-in/', views.checkIn, name='checkIn'),
    url(r'^check-out/', views.checkOut, name='checkOut'),
    url(r'^register-host/', views.hostRegistration, name='hostRegistration'),
]
