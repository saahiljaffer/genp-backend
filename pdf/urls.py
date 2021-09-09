from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^generate/$', views.generate_pdf, name='generate_pdf'),
]