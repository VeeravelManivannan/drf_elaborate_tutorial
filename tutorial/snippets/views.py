from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from snippets.models import Snippet
from snippets.serializers import SnippetSerializer
from rest_framework import status
from rest_framework.response import Response

# Create your views here.


@api_view(['GET','POST'])
def snippet_list(request,format=None):
    if request.method == 'GET':
        snippetObjectsList = Snippet.objects.all()
        snippetListSerializer = SnippetSerializer(snippetObjectsList , many=True )
        return Response(snippetListSerializer.data)
    elif request.method == 'POST':
        deserializer = SnippetSerializer(data=request.data)
        if deserializer.is_valid():
            deserializer.save()
            return Response(deserializer.data,status.HTTP_201_CREATED)
        return Response(deserializer.data,status.HTTP_400_BAD_REQUEST)
@api_view(['GET','PUT','DELETE'])
def snippets(request,pk,format=None):
   #this api is only for reading(so far 11-Aug-2019) , updating an existing and deleting an existing 
    try:
        snippet = Snippet.objects.get(pk=pk)
    except Snippet.DoesNotExist:
        return Response(status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        snippetSerializer = SnippetSerializer(snippet)
        return Response(snippetSerializer.data);
    elif request.method == 'PUT':
        snippetDeserializer = SnippetSerializer(data=request.data)
        if snippetDeserializer.is_valid():
            snippetDeserializer.save()
            return Response(status.HTTP_201_CREATED)
        return Response(deserializer.data,status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)









''' To be deleted , because there is going to be  a new API view

#This view is for displaying the snippet list
@csrf_exempt
def snippet_list(request):
    if request.method == 'GET':
        snippets = Snippet.objects.all()
        #In this scenarios , the constructor is created with multiple model objects
        serializer = SnippetSerializer(snippets, many=True)
        #This json response contains multiple Objects serialised and displayed in json 
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = SnippetSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

'''

'''

#This view is on displaying a single object of snippet
@csrf_exempt
def snippet_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        snippet = Snippet.objects.get(pk=pk)
    except Snippet.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = SnippetSerializer(snippet)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = SnippetSerializer(snippet, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        snippet.delete()
        return HttpResponse(status=204)    
       
'''
    
