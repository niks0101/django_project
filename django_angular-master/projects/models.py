from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User

class Project(models.Model):
    project_title = models.CharField(max_length=100)
    project_description = models.TextField()
    project_author_name = models.CharField(max_length=100)
    project_version = models.DecimalField(max_digits=4, decimal_places=2)
    user=models.ForeignKey(User,related_name='projects', on_delete=models.CASCADE)

class QuestionSet(models.Model):
    project = models.ForeignKey(Project,  related_name='questionset', on_delete=models.CASCADE)
    questionset_title = models.CharField(max_length=500)
    document = models.FileField(upload_to='documents/')
    comment = models.CharField(max_length=250)
    questionset_result = models.IntegerField(default=1)

class UserQuestion(models.Model):
    question_title = models.CharField(max_length=1000)
    default_value= models.BooleanField(default=False)


class UserQuestionAnswer(models.Model):
     questions = models.ForeignKey(QuestionSet, related_name='questions', on_delete=models.CASCADE)
     userquestion = models.OneToOneField(UserQuestion, related_name='userquestion', on_delete=models.CASCADE)
     question_answer = models.BooleanField()
     answer_option=models.IntegerField(default=1)
     comment = models.CharField(max_length=250)




