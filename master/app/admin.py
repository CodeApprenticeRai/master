from django.contrib import admin
from .models import User, Course, InstructorRole, Challenge, Question, QuestionChoice

admin.site.register(User)
admin.site.register(Course)
admin.site.register(InstructorRole)
admin.site.register(Challenge)
admin.site.register(Question)
admin.site.register(QuestionChoice)

# Register your models here.
