from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('sign_up/', views.sign_up, name="sign_up"),
    path('login/', views.login, name="login"),
    path('logout/', views.logout, name="logout"),
    path('home/course/skill/challenge/<int:challenge_id>/', views.challenge, name="challenge"),
    path(r'home/course/skill/challenge/preview/<int:challenge_id>', views.challenge, name="preview_challenge"),
    path('home/challenges', views.view_challenges, name="view_challenges"),
    path('challenge/', views.create_new_challenge, name="create_new_challenge"),
    path('challenge/<int:challenge_id>', views.edit_challenge, name="edit_challenge"),
    path('home/challenge/edit_question/delete/<int:question_id>', views.delete_question, name="delete_question"), # !! updating existing question, currently just for deleting question
    path('home/challenge/edit_question/<int:challenge_id>', views.edit_question, name="edit_question") #creating a new question
]
