from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import *
import app.forms


from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import logout as django_logout, authenticate, login as django_login
from django.contrib import messages

def index(request):
    if request.user.is_authenticated:
        return redirect('view_challenges')
    else:
        return render(request, 'app/intro_page.html')


def sign_up(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user_obj = form.save()
            username  = form.cleaned_data.get('username')
            django_login(request, user_obj)
            return redirect("index")
        else:
            return HttpResponse("Sign Up Failed.")

    sign_up_form = UserCreationForm()

    sign_up_form.fields['username'].help_text = '<br/> You can use letter, numbers, & characters (@/./+/-/_ ) <br/> '
    sign_up_form.fields['password1'].help_text = '<br/> Use 8 or more characters with a mix of letters, numbers, ' \
                                                 'and symbols <br/> <br/> Do NOT use any identifying information <br/> '
    sign_up_form.fields['password2'].help_text = None

    #for fieldname in ['username', 'password1', 'password2']:
       # sign_up_form.fields[fieldname].help_text = None

    context = {
        "form": sign_up_form
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
                return redirect('index')
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

@login_required
def view_challenges(request):
    ID_OF_DEFAULT_SKILL = 2 # !!
    skill_obj = Skill.objects.get(id=ID_OF_DEFAULT_SKILL) # !!
    print(skill_obj)
    challenges = Challenge.objects.filter(parent_skill=skill_obj)

    context={
    "skill": skill_obj,
    "challenges": challenges
    }

    return render(request, 'app/challenge_dashboard.html', context)

@login_required
def challenge(request, challenge_id):
    challenge_obj = Challenge.objects.get(pk=challenge_id)
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
            'challenge': challenge_obj,
            'correct_answer_count': correct_answer_count,
            'form_question_count': form_question_count,
            'percentage_correct': round( (correct_answer_count /  form_question_count) * 100, 2)
        }

        return render(request, 'app/challenge_report.html', context)

    else:

        context = {
            "challenge": challenge_obj,
            "form": app.forms.ChallengePresentationalForm(challenge_id)
        }

        preview = "preview" in request.path

        if preview:
            context["preview"] = True

        return render(request, 'app/challenge.html', context)

@login_required
def create_new_challenge(request):
    next_unclaimed_challenge_id = Challenge.objects.latest('id').id + 1
    return redirect('edit_challenge', challenge_id=next_unclaimed_challenge_id)


# Creation and Editing of Challenges
@login_required
def edit_challenge(request, challenge_id):
    referenced_challenge_exists = len(Challenge.objects.filter(id=challenge_id)) > 0

    challenge_obj = Challenge.objects.get(id=challenge_id) if referenced_challenge_exists else Challenge(id=challenge_id)

    if request.method == "POST": # try to create or update
        if request.POST.get('update-challenge-name', False):
            challenge_obj.name = request.POST['name']
            challenge_obj.save()
            referenced_challenge_exists = len(Challenge.objects.filter(id=challenge_id)) > 0
            messages.success(request, "Challenge name successfully updated to '{}'".format(challenge_obj.name))
        if request.POST.get('delete-challenge', False):
            challenge_obj.delete()
            return redirect('index')

    challenge_question_set = Question.objects.filter(parent_challenge=challenge_obj)

    form_initial_values = {"name": challenge_obj.name } if referenced_challenge_exists else {}
    challenge_form = app.forms.ChallengeForm(instance=challenge_obj, initial=form_initial_values)
    challenge_form.fields['name'].label = "Challenge Name"
    context = {
        'challenge_name_form': challenge_form,
        'challenge_button_action_label': 'Update Challenge Name' if referenced_challenge_exists else 'Create New Challenge',
        "questions":  challenge_question_set,
        "referenced_challenge_exists": referenced_challenge_exists
    }
    return render(request, 'app/edit_challenge.html', context)



@login_required
def edit_question(request, challenge_id):
    associated_challenge_obj = Challenge.objects.get(id=challenge_id)
    if request.method == 'POST':
        # parse question title and quesiton choices, validate then save, redirect to another empty form
        if request.POST.get('add-another', False):
            question_title = request.POST.get('text', [None])
            question_choices = request.POST.getlist('form-0-text')
            question_correct_answer = request.POST.get('correct-answer', '')

            if question_title and question_choices: #if they are not null, not empty
                quesion_obj = Question(parent_challenge=associated_challenge_obj, text=question_title)
                quesion_obj.save()


                #confirm question obj
                for question_choice_text in question_choices:
                    print(question_choice_text)
                    is_question_answer = question_choice_text == question_correct_answer
                    question_choice_obj = QuestionChoice(parent_question=quesion_obj, text=question_choice_text, correct_answer=is_question_answer)
                    question_choice_obj.save()

            messages.success(request, "Question successfully created and added to challenge")

    context = {
        'question_title_form': app.forms.QuestionModelForm(),
        'question_choice_formset': app.forms.QuestionChoiceFormset(request.GET or None),
        'challenge': associated_challenge_obj
    }
    return render(request, 'app/edit_question.html', context)

@login_required
def delete_question(request, question_id):
    query_result_set = Question.objects.filter(id=question_id)

    if ( query_result_set ):
        parent_challenge_obj = query_result_set[0].parent_challenge
        query_result_set[0].delete()
        return redirect('edit_challenge', challenge_id=parent_challenge_obj.id)

    else:
        return redirect('index')

@login_required
def view_challenge_analytics(request, challenge_id):
    context = {}
    return render(request, 'app/challenge_analytics.html', context)
