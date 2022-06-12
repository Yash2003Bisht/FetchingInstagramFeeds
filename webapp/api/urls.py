from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_data),
    path('add/', views.post_data),
]
