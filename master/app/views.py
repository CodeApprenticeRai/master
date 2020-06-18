from django.http import HttpResponse
from django.shortcuts import render
from .models import User, Course, InstructorRole, Challenge, Question, QuestionChoice
import app.forms

def index(request):
    return HttpResponse("suc suc suc suc suc suc suc")

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
