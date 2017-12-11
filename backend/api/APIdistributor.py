from rest_framework.generics import (
	CreateAPIView,		
	ListAPIView,	
	UpdateAPIView,		
	DestroyAPIView,	
	ListCreateAPIView,	
	GenericAPIView
)
from rest_framework import status
from rest_framework.response import Response
from rest_framework.exceptions import (APIException)

from backend.models import Distributor
from backend.serializers.Serializerdistributor import SelectDistributor
from rest_framework import permissions

class SelectAllDistributor(ListAPIView):
	
	permission_classes = []
	
	def get_queryset(self):
		return Distributor.objects.all()[:5]

	def get_serializer_class(self):
		return SelectDistributor


class loginview(GenericAPIView):
	
	permission_classes = []
	
	def post(self, request):

		if Distributor.objects.filter(umail= request.POST.get('email'), pswd= request.POST.get('password')).exists():
			return Response({'email':request.POST.get('email')}, status=status.HTTP_200_OK)
		return Response({'detail':'email and password not match'}, status=status.HTTP_400_BAD_REQUEST)

	def get_serializer_class(self):
		return SelectDistributor