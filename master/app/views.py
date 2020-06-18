from django.http import HttpResponse
from django.shortcuts import render
from .models import User, Course, InstructorRole, Challenge, Question, QuestionChoice
import app.forms

def index(request):
    return render(request, 'app/index.html')

def challenge(request, challenge_id):
    # try:
    challenge_obj = Challenge.objects.get(pk=challenge_id)
    course_obj = challenge_obj.parent_course

    context = {
        "course": course_obj,
        "challenge": challenge_obj,
        "form": app.forms.ChallengeForm(challenge_id)
    }

    return render(request, 'app/challenge.html', context)
