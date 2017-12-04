from rest_framework.generics import (
	CreateAPIView,		
	ListAPIView,		
	UpdateAPIView,		
	DestroyAPIView,		
)
from rest_framework.exceptions import (APIException)

from backend.models import User
from backend.serializers.Serializeruser import UserSerializer
from rest_framework import permissions

class ReadUser(ListAPIView):

	def get_queryset(self):
		return User.objects.all()

	def get_serializer_class(self):
		return UserSerializer

class RegisterUser(CreateAPIView):
	serializer_class = UserSerializer
	permission_classes = []
	def get_queryset(self):
		return None
	# def get_serializer_class(self):
	# 	return UserSerializer
	def get_queryset(self):
		return User.objects.filter(pk = 2)

	def perform_create(self, serializer):
		username = self.request.POST.get('user')
		if username == '' or username is None:
			raise APIException('username is required field')
		serializer.save(
			username = self.request.POST.get('user'),
			pswd = self.request.POST.get('pwd'),
			umail = self.request.POST.get('email'),
			nama_lengkap = self.request.POST.get('fullname'),
			jabatan = self.request.POST.get('position'),
		)

class UpdateUser(UpdateAPIView):
	lookup_field = 'username'
	permission_classes = []
	def get_queryset(self):
		return User.objects.all()

	def get_serializer_class(self):
		return UserSerializer

	def perform_update(self, serializer):
		# raise APIException(serializer)
		username = self.request.POST.get('user')
		if username == '' or username is None:
			raise APIException('username is required field')

		serializer.save(
			username = self.request.POST.get('user'),
			pswd = self.request.POST.get('pwd'),
			umail = self.request.POST.get('email'),
			nama_lengkap = self.request.POST.get('fullname'),
			jabatan = self.request.POST.get('position'),
		)