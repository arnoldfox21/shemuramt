from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    UpdateAPIView
)
from rest_framework import status
from rest_framework.response import Response
from rest_framework.exceptions import (APIException)

from django.shortcuts import get_object_or_404
from backend.models import Companyprofile
from backend.serializers.Serializercompanyprofile import Info
from rest_framework import permissions


class AboutCompany(ListAPIView):

    permission_classes = []
    serializer_class = Info

    def list(self, request, *args, **kwargs):
        queryset = get_object_or_404(
            self.get_queryset(),
            pk=self.kwargs.get('uid')
        )

        serializer = self.get_serializer(queryset)
        return Response(serializer.data)

    def get_queryset(self):

        return Companyprofile.objects.all()
