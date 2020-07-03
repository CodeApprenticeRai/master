from django.contrib import admin
from .models import *

admin.site.register(Course)
admin.site.register(InstructorRole)
admin.site.register(Challenge)
admin.site.register(Question)
admin.site.register(QuestionChoice)
admin.site.register(Skill)
# Register your models here.
