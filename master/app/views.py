from django.http import HttpResponse
from django.shortcuts import render
from .models import User, Course, InstructorRole, Challenge, Question, QuestionChoice

def index(request):
    return HttpResponse("suc suc suc suc suc suc suc")

def challenge(request, challenge_id):
    # try:
    challenge_obj = Challenge.objects.get(pk=challenge_id)
    questions_query_set = Question.objects.filter(parent_challenge=challenge_obj)


    questions = { int(question.id) : { "question": question } for question in questions_query_set if not print(question.id) }

    for question_id in questions:
         questions[int(question_id)]["choices"] = QuestionChoice.objects.filter(parent_question=questions[question_id]["question"])

    context = {
        "challenge": challenge_obj,
        "questions": questions
    }

    return render(request, 'app/challenge.html', context)
    # except:
        # return HttpResponse(status=500)

def sign_up(request):
    return render(request, 'app/sign_up.html')


def login(request):
    return render(request, 'app/login.html')


