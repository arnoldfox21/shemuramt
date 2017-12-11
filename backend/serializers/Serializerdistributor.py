from rest_framework import serializers
from backend.models import Distributor


class SelectDistributor(serializers.ModelSerializer):

    class Meta:
        model = Distributor
        fields = [
            'id',
            'nama',
            'umail',
            'alamat',
            'joined_time',
            'foto',
            'pswd'
        ]