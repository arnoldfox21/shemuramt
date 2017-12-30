from rest_framework import serializers
from backend.models import Barang


class SelectItem(serializers.ModelSerializer):
 
    class Meta:
        model = Barang
        fields = [
            'id',
            'harga_satuan',
            'nm_barang',
            'stock',
            'berat',
            'warna'
        ]

