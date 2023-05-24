from django.urls import path
from . import views

app_name = 'planets'

urlpatterns = [
    path('', views.main, name='main'),
    path('planets/', views.planet_list, name='planet_list'),
    path('planets/create/', views.planet_create, name='planet_create'),
    path('planets/<str:planet_name>/join/', views.planet_join, name='planet_join'),
    path('planets/<str:planet_name>/', views.index, name='index'),
    path('planets/<str:planet_name>/<int:post_pk>/delete/', views.post_delete, name='post_delete'),
]
