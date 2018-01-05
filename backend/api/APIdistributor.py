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
from django.shortcuts import get_object_or_404

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
    serializer_class = SelectDistributor

    def post(self, request, *args, **kwargs):
        queryset = get_object_or_404(
            self.get_queryset(),
            umail=request.POST.get('mail'),
            pswd=request.POST.get('pass')
        )

        serializer = self.get_serializer(queryset)
        return Response(serializer.data)

    def get_queryset(self):
        return Distributor.objects.all()