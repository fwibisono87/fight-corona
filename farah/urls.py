from django.urls import path

from . import views

app_name = 'farah'

urlpatterns = [
    path('', views.edukasi, name='edukasi'),
    path('listkegiatan/', views.listkegiatan, name='listkegiatan'),
]
