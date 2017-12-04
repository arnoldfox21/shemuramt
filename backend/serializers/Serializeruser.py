from rest_framework import serializers
from backend.models import User


class UserSerializer(serializers.ModelSerializer):
    email = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = [
            'username',
            'nama_lengkap',
            'jabatan',
            'email',
        ]

    def get_email(self, obj):
        return obj.umail