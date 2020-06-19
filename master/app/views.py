from django.http import HttpResponse
from django.shortcuts import render
from .models import User, Course, InstructorRole, Challenge, Question, QuestionChoice
import app.forms

def index(request):
    return render(request, 'app/index.html')

def challenge(request, challenge_id):
    challenge_obj = Challenge.objects.get(pk=challenge_id)
    course_obj = challenge_obj.parent_course

    context = {
        "course": course_obj,
        "challenge": challenge_obj,
        "form": app.forms.ChallengeForm(challenge_id)
    }

    return render(request, 'app/challenge.html', context)

def instructor_course_view(request, instructor_id):
    # get instructor object
    instructor_obj = User.objects.get(id=instructor_id)

    # extract associated_courses
    courses_led_by_instructor = [ role_object.associated_course for role_object in InstructorRole.objects.filter(associated_user=instructor_obj) ]

    # add courses to context
    context = {
        "insturctor": instructor_obj,
        "courses": courses_led_by_instructor
    }

    return render(request, 'app/instructor_course_view.html', context)
