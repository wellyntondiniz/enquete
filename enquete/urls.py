from enquete import views
from django.urls import path

app_name = 'enquete'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:id_questao>/votar', views.votar, name='votar'),
    path('<int:id_questao>/resultados', views.resultados, name='resultados'),
]