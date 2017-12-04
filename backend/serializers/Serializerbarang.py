from rest_framework import serializers
from backend.models import Barang


class select_item(serializers.ModelSerializer):
    item = serializers.SerializerMethodField()
    class Meta:
        model = Barang
        fields = [
            'id',
            'harga_satuan',
            'item',
        ]

    def get_item(self, obj):
        return obj.nm_barang
