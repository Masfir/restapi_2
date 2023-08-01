from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from myapp.models import Contact
from myapp.serializers import ContactSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

# Create your views here.

@api_view(['GET', 'POST'])
def api_list(request):
    if request.method == 'GET':
        api_view = Contact.objects.all()
        serializer = ContactSerializer(api_view, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ContactSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET', 'PUT', 'DELETE'])
def api_detail(request,pk):
    try:
        api_view = Contact.objects.get(pk=pk)
    except Contact.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ContactSerializer(api_view)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ContactSerializer(api_view, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        api_view.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)