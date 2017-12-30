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
			f = getb.first()
			return Response({'id': f.id,'nama_barang': f.nm_barang, 'harga_satuan': f.harga_satuan, 'stock': f.stock, 'warna': f.warna}, status=status.HTTP_200_OK)
		else:
			return Response({"recieved": request.POST.get('id')}, status=status.HTTP_400_BAD_REQUEST)
	def get_serializer_class(self):
		return SelectItem