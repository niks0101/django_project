from rest_framework import serializers
from .models import Project,QuestionSet,UserQuestionAnswer,UserQuestion
from django.contrib.auth.models import User



class UserQuestionSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserQuestion
        fields = ('id','question_title','default_value')


class UserQuestionAnswerSerializer(serializers.ModelSerializer):
    userquestion = UserQuestionSerializer()
    id = serializers.IntegerField(required=False)
    class Meta:
        model = UserQuestionAnswer
        fields = ('id','userquestion','question_answer','answer_option','comment')

class QuestionSetSerializer(serializers.ModelSerializer):
    questions = UserQuestionAnswerSerializer(many=True,read_only=False)
    class Meta:
        model = QuestionSet
        fields = ('id','questionset_title','comment','questions','questionset_result')
    def update(self,instance, validated_data):
        count=0
        count1=0
        count2=0
        count3=0
        count4=0
        # Create or update page instances that are in the request
        for item in validated_data['questions']:
            userQuestionAnswer_item = UserQuestionAnswer.objects.get(questions=instance, pk=item.get('id'))
            userQuestionAnswer_item.question_answer = item.get('question_answer', userQuestionAnswer_item.question_answer)
            userQuestionAnswer_item.answer_option = item.get('answer_option', userQuestionAnswer_item.answer_option)
            userQuestionAnswer_item.comment = item.get('comment', userQuestionAnswer_item.comment)
            userQuestionAnswer_item.save()

        for item in validated_data['questions']:
            userQuestionAnswer_item = UserQuestionAnswer.objects.get(questions=instance, pk=item.get('id'))
            if(userQuestionAnswer_item.answer_option ==1):
                  count=count+1;
            elif(userQuestionAnswer_item.answer_option ==2):
                  count1=count1+1;
            elif(userQuestionAnswer_item.answer_option ==3):
                  count3=count3+1;
            elif(userQuestionAnswer_item.answer_option ==4):
                  count4=count4+1;
            else:
                  count2=count2+1;
        if(count2>=1):
            instance.questionset_result=5
        elif(count4>=1):
            instance.questionset_result=4
        elif(count1>=1):
            instance.questionset_result=2
        elif(count>=1):
            instance.questionset_result=1
        elif(count3>=1):
            instance.questionset_result=3

        instance.comment = validated_data.get('comment', instance.comment)

        instance.save()
        return instance

class ProjectSerializer(serializers.ModelSerializer):
    questionset = QuestionSetSerializer(many=True,read_only=False)
    class Meta:
        model = Project
        fields = ('id','project_title', 'project_description', 'project_author_name', 'project_version','user_id','questionset')

class UserSerializer(serializers.ModelSerializer):
    projects = ProjectSerializer(many=True,read_only=False)

    class Meta:
        model = User
        fields = ('id', 'username', 'projects')


