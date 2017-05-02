from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from .serializers import ProjectSerializer,QuestionSetSerializer,UserQuestionAnswerSerializer,UserQuestionSerializer
from .models import Project,QuestionSet,UserQuestionAnswer,UserQuestion
import json

class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

@csrf_exempt
def project_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        snippets = Project.objects.all()
        serializer = ProjectSerializer(snippets, many=True)
        return JSONResponse(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ProjectSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)

@csrf_exempt
def project_detail(request, pk):
    """
    Retrieve, update or delete a code project.
    """
    try:
        project = Project.objects.get(pk=pk)
    except Project.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = ProjectSerializer(project)
        return JSONResponse(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ProjectSerializer(project, data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        project.delete()
        return HttpResponse(status=204)

@csrf_exempt
def questionset_detail(request, pk):
    """
    Retrieve, update or delete a code project.
    """
    try:
        questionset = QuestionSet.objects.get(pk=pk)
    except QuestionSet.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = QuestionSetSerializer(questionset)
        return JSONResponse(serializer.data)

    elif request.method == 'POST':
        data = json.loads(request.POST['questionset'])
        serializer = QuestionSetSerializer(questionset, data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        questionset.delete()
        return HttpResponse(status=204)
