from django.urls import path
from . import views

urlpatterns = [
    path('home/',views.home),
    path('contact/',views.contact),
    path('about/<int:n>',views.about),
    path('service/',views.service),
]