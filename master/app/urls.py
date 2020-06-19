from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('challenge/<int:challenge_id>/', views.challenge, name="challenge"),
    path('course/<int:course_id>', views.instructor_view_course_skills, name="instructor_view_course_skills"), # !! variable names should also be changed
    path('courses/<int:instructor_id>', views.instructor_view_courses, name="instructor_view_courses"), # !! needs to be changed, use sesisons
    path('course/skill/challenges/<int:skill_id>', views.instructor_view_skill_challenges, name="instructor_view_skill_challenges" ) # !! required changes related to above notes
]
