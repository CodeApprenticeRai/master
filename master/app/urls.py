from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('sign_up/', views.sign_up, name="sign_up"),
    path('login/', views.login, name="login"),
    path('logout/', views.logout, name="logout"),
    path('home/', views.home, name="home"),
    path('home/course//skill/challenge/<int:challenge_id>/', views.challenge, name="challenge"),
    path('home/course/<int:course_id>', views.course_view, name="course_view"), # Render all the skills of a specified course
    path('home/course/skill/<int:skill_id>', views.skill_view, name="skill_view" ) # Render all the skills of a specified course
]
