from rest_framework.generics import (
	CreateAPIView,		
	ListAPIView,	
	UpdateAPIView,		
	DestroyAPIView,		
)

from rest_framework.exceptions import (APIException)
from backend.models import Pembelian
from backend.serializers.Serializersupplier import Pembelian
from rest_framework import permissions

class OrderBahan(CreateAPIView):

	permission_classes = []
	def get_quesryset(self):
		return None

	def get_serializer_class(self):
		return Pembelian

	def get_queryset(self):
		return Pembelian.objects.filter()

	def perform_create(self, serializer):
	
		if self.request.POST.get('n') != '0':
			serializer.save(
				jumlah = self.request.POST.get('n'),
				bahan_id = '1',
			)
		# if self.request.POST.get('pk') != '0':
		# 	serializer.save(
		# 		jumlah = self.request.POST.get('pk'),
		# 		bahan_id = '2',
		# 	)
		# if self.request.POST.get('mn') != '0':
		# 	serializer.save(
		# 		jumlah = self.request.POST.get('mn'),
		# 		bahan_id = '3',
		# 	)
		