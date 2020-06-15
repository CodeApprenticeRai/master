from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('challenge/<int:challenge_id>/', views.challenge, name="challenge")
]
