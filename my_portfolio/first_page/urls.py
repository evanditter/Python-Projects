from django.urls import path
from first_page import views

urlpatterns = [
    path('', views.first_page, name='first_page'),
]
