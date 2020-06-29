from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import *
import app.forms

from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import logout as django_logout, authenticate, login as django_login


def index(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        return render(request, 'app/intro_page.html')


def sign_up(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user_obj = form.save()
            username = form.cleaned_data.get('username')
            django_login(request, user_obj)
            return redirect("home")
        else:
            return HttpResponse("Something silly happened.")
    context = {
        "form": UserCreationForm
    }

    return render(request, 'app/sign_up.html', context)


def login(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                django_login(request, user)
                # messages.info(request, f"You are now logged in as {username}")
                return redirect('home')
            else:
                pass
                # messages.error(request, "Invalid username or password.")
        else:
            pass
            # messages.error(request, "Invalid username or password.")

    context = {
        'form': AuthenticationForm
    }

    return render(request, 'app/login.html', context)


def logout(request):
    if request.user.is_authenticated:
        django_logout(request)
        # messages.info(request, "Logged out successfully!")

    return redirect('index')


def challenge(request, challenge_id):
    if request.method == 'POST':
        # !! does not generalize,
        # assumes that all keys in request.POST
        # is a form_question
        form_question_count = 0
        correct_answer_count = 0

        # print(request.POST)
        for form_question in request.POST:
            if (form_question == "csrfmiddlewaretoken"):
                continue

            user_choice_id = request.POST[form_question]
            choice_obj = QuestionChoice.objects.get(id=user_choice_id)

            print([choice_obj.id, choice_obj.text, choice_obj.correct_answer])
            if (choice_obj.correct_answer):
                correct_answer_count += 1

            form_question_count += 1

        context = {
            'correct_answer_count': correct_answer_count,
            'form_question_count': form_question_count,
            'percentage_correct': (correct_answer_count / form_question_count) * 100
        }

        return render(request, 'app/challenge_report.html', context)

    else:
        challenge_obj = Challenge.objects.get(pk=challenge_id)

        context = {
            "challenge": challenge_obj,
            "form": app.forms.ChallengeForm(challenge_id)
        }
        return render(request, 'app/challenge.html', context)


# !! For now ( until moving to sessions ) : Given an instructor_id,
# return tablelists of all courses that user is an instructor of
@login_required
def home(request):
    if not request.user:
        return HttpResponse("The user is not bound to session, debug this.")

    # get instructor object
    instructor_obj = request.user

    # add Course
    if request.method == 'GET':
        if request.GET.get("Add Course"):
            temp = request.GET['name']
            if Course.objects.filter(name=temp).exists():
                print("Course name already exists...")
            else:
                addCourse = Course(name=temp)
                addI_Role = InstructorRole(associated_user=instructor_obj, associated_course=addCourse)
                addCourse.save()
                addI_Role.save()

        if request.GET.get(value="Remove Course"):
            print(request.GET)
            Course.objects.filter(pk=Course.id).delete()

    # extract associated_courses
    courses_led_by_instructor = [role_object.associated_course for role_object in
                                 InstructorRole.objects.filter(associated_user=instructor_obj)]
    # remove Course
    if request.method == 'POST':
        print(request.POST)
        if request.POST.get("Remove Course"):
            Course.objects.filter(pk=Course.id).delete()

    # add courses to context
    context = {
        "instructor": instructor_obj,
        "courses": courses_led_by_instructor,
        "form": app.forms.AddCourseForm()
    }

    return render(request, 'app/home.html', context)


# Render all the skills of a specified course
@login_required
def course_view(request, course_id):
    course_obj = Course.objects.get(id=course_id)
    skills = Skill.objects.filter(parent_course=course_obj)

    if request.GET:

        if request.GET.get("Add Skill"):
            temp = request.GET['name']
            if Skill.objects.filter(name=temp, parent_course=course_obj).exists():
                print("Skill name already exists for this Course...")
            else:
                addSkill = Skill(name=temp, parent_course=course_obj)
                addSkill.save()
        if request.GET.get("Remove Skill"):
            print(request.GET)

    context = {
        "course": course_obj,
        "skills": skills,
        "form": app.forms.AddSkillForm()
    }

    return render(request, 'app/course_view.html', context)


@login_required
def skill_view(request, skill_id):
    skill_obj = Skill.objects.get(id=skill_id)
    challenges = Challenge.objects.filter(parent_skill=skill_obj)

    context = {
        "skill": skill_obj,
        "challenges": challenges
    }

    return render(request, 'app/skill_view.html', context)
