from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializer import*;
# Create your views here.

@api_view(['GET'])
def GetAllEmployees(request):
    users = Book.objects.all()

    serial = Bookserial(users,many=True)
    return Response(serial.data)

@api_view(['GET'])
def one_data(request,pk):
    
    users = Book.objects.get(id=pk)

    serial = Bookserial(users)
    return Response(serial.data)


@api_view(['POST'])
def create_data(request):

    serial = Bookserial(data=request.data)

    if serial.is_valid():
        serial.save()

        return Response(serial.data)

@api_view(['GET','PUT'])
def update_data(request,pk):
    user = Book.objects.get(id=pk)
    if request.method == 'PUT':
        serial = Bookserial(instance=user,data=request.data)

        if serial.is_valid():
            serial.save()

            return Response(serial.data)

    serial = Bookserial(user)
    return Response(serial.data)

@api_view(['DELETE','GET'])
def delete_data(request,pk):
    try:
        user = Book.objects.get(id=pk)
        if request.method == 'DELETE':
            try:
                user.delete()
                return Response('Data Deleted')
            except:
                return Response('Data not Found')
        serial = Bookserial(user)
        return Response(serial.data)
    except:
        return Response('Invalid Id')


