from django.contrib import admin
from .models import Project, QuestionSet,UserQuestion,UserQuestionAnswer

admin.site.register(Project)
admin.site.register(QuestionSet)
admin.site.register(UserQuestion)
admin.site.register(UserQuestionAnswer)
