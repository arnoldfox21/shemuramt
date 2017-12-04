from rest_framework.generics import (
	CreateAPIView,		
	ListAPIView,	
	UpdateAPIView,		
	DestroyAPIView,		
)
from rest_framework.exceptions import (APIException)

from backend.models import Barang
from backend.serializers.Serializerbarang import select_item
from rest_framework import permissions

class SelectAll(ListAPIView):
	
	permission_classes = []
	def perform_all(self, serializer):
		fd = self.request.POST.get('idb')

	def get_queryset(self):
		return Barang.objects.all()

	def get_serializer_class(self):
		return select_item
		
class Selectitem(ListAPIView):
	lookup_field = 'id'
	permission_classes = []

	def get_queryset(self, serializer):
		id_item = self.request.POST.get('id')
		if id_item == '':
			raise APIException('id is required')
		else:
			return Barang.objects.filter(pk = id_item)

	def get_serializer_class(self):
		return select_item