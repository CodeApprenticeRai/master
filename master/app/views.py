from django.http import HttpResponse
from django.shortcuts import render
from .models import *
import app.forms


def index(request):
    return render(request, 'app/index.html')


def challenge(request, challenge_id):
    if request.method == 'POST':
        # !! does not generalize,
        # assumes that all keys in request.POST
        # is a form_question
        form_question_count = 0
        correct_answer_count = 0

        # print(request.POST)
        for form_question in request.POST:
            if form_question == "csrfmiddlewaretoken":
                continue

            user_choice_id = request.POST[form_question]
            choice_obj = QuestionChoice.objects.get(id=user_choice_id)

            print([choice_obj.id, choice_obj.text, choice_obj.correct_answer])
            if choice_obj.correct_answer:
                correct_answer_count += 1

            form_question_count += 1

        # generate scorecard
        chal = Challenge.objects.get(id=challenge_id)
        perc = ((correct_answer_count / form_question_count) * 100)
        grade = Scorecard(chal, request.user.id, perc)

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

def instructor_view_courses(request, instructor_id):
    # get instructor object
    instructor_obj = User.objects.get(id=instructor_id)

    # extract associated_courses
    courses_led_by_instructor = [role_object.associated_course for role_object in
                                 InstructorRole.objects.filter(associated_user=instructor_obj)]

    # add courses to context
    context = {
        "instructor": instructor_obj,
        "courses": courses_led_by_instructor
    }

    return render(request, 'app/instructor_view_courses.html', context)


def instructor_view_course_skills(request, course_id):
    course_obj = Course.objects.get(id=course_id)
    skills = Skill.objects.filter(parent_course=course_obj)

    context = {
        "course": course_obj,
        "skills": skills
    }

    return render(request, 'app/instructor_view_course_skills.html', context)


def instructor_view_skill_challenges(request, skill_id):
    skill_obj = Skill.objects.get(id=skill_id)
    challenges = Challenge.objects.filter(parent_skill=skill_obj)
    # grade = Scorecard.objects.filter()

    context = {
        "skill": skill_obj,
        "challenges": challenges
    }

    return render(request, 'app/instructor_view_skill_challenges.html', context)


def instructor_view_courses(request, instructor_id):
    # get instructor object
    instructor_obj = User.objects.get(id=instructor_id)

    # extract associated_courses
    courses_led_by_instructor = [role_object.associated_course for role_object in
                                 InstructorRole.objects.filter(associated_user=instructor_obj)]

    # add courses to context
    context = {
        "instructor": instructor_obj,
        "courses": courses_led_by_instructor
    }

    return render(request, 'app/instructor_view_courses.html', context)


def instructor_view_course_skills(request, course_id):
    course_obj = Course.objects.get(id=course_id)
    skills = Skill.objects.filter(parent_course=course_obj)

    context = {
        "course": course_obj,
        "skills": skills
    }

    return render(request, 'app/instructor_view_course_skills.html', context)


def instructor_view_skill_challenges(request, skill_id):
    skill_obj = Skill.objects.get(id=skill_id)
    challenges = Challenge.objects.filter(parent_skill=skill_obj)
    # grade = Scorecard.objects.filter()

    context = {
        "skill": skill_obj,
        "challenges": challenges
    }

    return render(request, 'app/instructor_view_skill_challenges.html', context)
