from django.db import models
from django.contrib.auth.models import User


class Course(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class InstructorRole(models.Model):
    associated_user = models.ForeignKey(User, on_delete=models.PROTECT)
    associated_course = models.ForeignKey(Course, on_delete=models.PROTECT)

    def __str__(self):
        return str(self.associated_user.username)


class Skill(models.Model):
    name = models.CharField(max_length=255)
    parent_course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.name)


class Challenge(models.Model):
    name = models.CharField(max_length=255)
    parent_skill = models.ForeignKey(Skill, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Question(models.Model):
    parent_challenge = models.ForeignKey(Challenge, on_delete=models.CASCADE)
    text = models.TextField()

    def __str__(self):
        return self.text


class QuestionChoice(models.Model):
    parent_question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.TextField()
    correct_answer = models.BooleanField()

    def __str__(self):
        return self.text
