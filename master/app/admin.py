from django.contrib import admin
from .models import *


admin.site.register(InstructorRole)
admin.site.register(Challenge)
admin.site.register(Question)
admin.site.register(QuestionChoice)
admin.site.register(CandidateRole)
admin.site.register(ChallengeReport)
admin.site.register(ChallengeReportQuestionSubmission)
# Register your models here.
