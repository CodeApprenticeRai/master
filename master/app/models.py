from django.db import models


class User(models.Model):
    name=models.CharField(max_length=200)
    #username
    #email
    #etc

    def __str__(self):
        return self.name

class Course(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
       return self.name

class InstructorRole(models.Model):
    associated_user=models.ForeignKey(User, on_delete=models.PROTECT)
    associated_course= models.ForeignKey(Course, on_delete=models.PROTECT)

    def __str__(self):
       return str(self.associated_user) #! this is a hack

class Challenge(models.Model):
    name = models.CharField(max_length=255)
    parent_course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
       return self.name

class Question(models.Model):
    parent_challenge = models.ForeignKey(Challenge, on_delete=models.CASCADE)
    text = models.TextField()

    def __str__(self):
       return self.text

class QuestionChoice(models.Model):
    parent_question = models.ForeignKey(Question, on_delete=models.CASCADE )
    text = models.TextField()

    def __str__(self):
       return self.text
