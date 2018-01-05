from rest_framework import serializers
from backend.models import Companyprofile


class Info(serializers.ModelSerializer):
 
    class Meta:
        model = Companyprofile
        fields = [
            'id',
            'about_post',
            'title',
            'description',
            'about_title',
        ]

