from django.urls import path
from . import views

urlpatterns = [
    path('',views.home),
    path('home/',views.home),
    path('about/',views.about),
    path('courses/',views.courses),
    path('trainers/',views.trainers),
    path('trainers/',views.trainers),
]
