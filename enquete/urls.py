from enquete import views
from django.urls import path

app_name = 'enquete'

urlpatterns = [
    path('', views.index, name='index')
]