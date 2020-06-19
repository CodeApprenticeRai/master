import django.forms as forms
from django.forms import ModelForm
import app.models as qm



class ChallengeForm(forms.Form):
    def __init__(self, challenge_id):
        forms.Form.__init__(self)

        challenge = qm.Challenge.objects.get(pk=challenge_id)

        questions = qm.Question.objects.filter(parent_challenge=challenge)


        for question_number, question in enumerate(questions):
            question_choices = qm.QuestionChoice.objects.filter(parent_question=question)

            django_formatted_choices = [ (choice.text, choice.text) for choice in question_choices ]

            question_display_title = '{}: {}'.format(question_number+1, question.text)
            self.fields[question_display_title] = forms.ChoiceField(choices=django_formatted_choices, widget=forms.RadioSelect)
            self.fields[question_display_title].required=True



        #
        #
        # for _id in id_indexed_question_choices:
        #     id_indexed_question_choices[_id] = [ choice.text for choice in id_indexed_question_choices[_id]  ]
        #
        # form_fields = [ forms.ChoiceField(label=question.text, choices=id_indexed_question_choices[question.id]) for question in questions ]
