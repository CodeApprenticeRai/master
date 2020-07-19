from django.db import models
from django.contrib.auth.models import User


class Challenge(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
       return self.name

class InstructorRole(models.Model):
   associated_instructor = models.ForeignKey(User, on_delete=models.PROTECT)
   associated_challenge = models.ForeignKey(Challenge, null=True, on_delete=models.PROTECT)

   def __str__(self):
       return str(self.associated_user.username)

   def is_instructor_of_challenge(self, user_id, challenge_id):
       if self.objects.filter(associated_instructor=user_id, associated_challenge=user_id):
           return True
       else:
           return False

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
