from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('challenge/<int:challenge_id>/', views.challenge, name="challenge"),
    path('courses/<int:instructor_id>', views.instructor_course_view, name="instructor_course_view")    
]
