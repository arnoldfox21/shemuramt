from rest_framework.generics import (
	CreateAPIView,		
	ListAPIView,	
	UpdateAPIView,		
	DestroyAPIView,	
	GenericAPIView
)
from rest_framework import status
from rest_framework.response import Response
from rest_framework.exceptions import (APIException)

from backend.models import Barang
from backend.serializers.Serializerbarang import SelectItem
from rest_framework import permissions

class SelectAll(ListAPIView):
	
	permission_classes = []
	def perform_all(self, serializer):
		fd = self.request.POST.get('idb')

	def get_queryset(self):
		return Barang.objects.all()

	def get_serializer_class(self):
		return SelectItem
		
class Selectitem(GenericAPIView):

	permission_classes = []

	def post(self, request):

		getb = Barang.objects.filter(pk = request.POST.get('id'))
		if getb.exists():
			return Response({'nama_barang': '2'}, status=status.HTTP_200_OK)
		else:
			return Response({"message": "What you were looking for isn't here."})
	def get_serializer_class(self):
		return SelectItem

	def empty_view(self):

	    content = {'please move along': 'nothing to see here'}
	    return Response(content, status=status.HTTP_404_NOT_FOUND)