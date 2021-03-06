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

from django.shortcuts import get_object_or_404
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


class Selectitem(ListAPIView):

    permission_classes = []
    serializer_class = SelectItem

    def list(self, request, *args, **kwargs):
        queryset = get_object_or_404(
            self.get_queryset(),
            pk=self.kwargs.get('uid')
        )

        serializer = self.get_serializer(queryset)
        return Response(serializer.data)

    def get_queryset(self):

        return Barang.objects.all()
