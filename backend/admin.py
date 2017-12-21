from django.contrib import admin
from backend.models import User, Suplier, Pembelian, Distributor, Transaksi, Barang, Keranjang, Contact, Fakthur, Session_distributor, Session_user, Contact_reply, Settings, Companyprofile

admin.site.register(User)
admin.site.register(Distributor)
admin.site.register(Transaksi)
admin.site.register(Barang)
admin.site.register(Keranjang)
admin.site.register(Contact)
admin.site.register(Fakthur)
admin.site.register(Session_distributor)
admin.site.register(Session_user)
admin.site.register(Contact_reply)
admin.site.register(Settings)
admin.site.register(Companyprofile)
admin.site.register(Pembelian)
admin.site.register(Suplier)