from rest_framework import serializers
from backend.models import Pembelian, Bahan


class Pembelian(serializers.ModelSerializer):
    bahan = serializers.SerializerMethodField()

    class Meta:
        model = Pembelian
        fields = [
            'jumlah',
            't_harga',
            'bahan',
        ]

    def get_bahan(self, obj):
        return obj.bahan_id
