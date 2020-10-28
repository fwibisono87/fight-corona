from django.urls import path

from . import views

app_name = 'jati'

urlpatterns = [
    path('', views.maskermu, name='maskermu'),
    # path('listkegiatan/', views.listkegiatan, name='listkegiatan'),
]
