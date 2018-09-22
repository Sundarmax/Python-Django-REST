from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import passengerSerializer,ticketSerializer,flightDSerializer,flightSerializer,cardSerializer
from .models import flight,flight_details,passenger_info,ticket_info,card_details

class flightViewSet(ModelViewSet):
    queryset = flight.objects.all()
    serializer_class = flightSerializer
class flightDViewSet(ModelViewSet):
    queryset = flight_details.objects.all()
    serializer_class = flightDSerializer
class passengerViewSet(ModelViewSet):
    queryset = passenger_info.objects.all()
    serializer_class = passengerSerializer
class ticketViewSet(ModelViewSet):
    queryset = ticket_info.objects.all()
    serializer_class = ticketSerializer
class cardViewSet(ModelViewSet):
    queryset = card_details.objects.all()
    serializer_class = cardSerializer

@api_view(['GET', 'POST','DELETE'])
def flight_listAll(request): 
    if request.method == 'GET':
        data = flight.objects.all()
        serializers = flightSerializer(data, many=True)
        return Response(serializers.data)
    elif request.method == 'POST':
         serializer = flightSerializer(data = request.data)
         if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
         else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)    
def flight_detail(request):
    if request.method == 'GET':
        data = flight_detail.objects.all()
        serializers = flightDSerializer(data, many=True)
        return Response(serializers.data)
    elif request.method == 'POST':
         serializer = flightDSerializer(data = request.data)
         if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
         else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def flight_list(request, pk):
    try:
        data = flight.objects.get(pk=pk)
    except flight.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = flightSerializer(data)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = flightSerializer(data, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)    
    elif request.method == 'DELETE':
        data.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    