from django import template
from backend.models import Keranjang, Session_user, Contact, Barang
from django.db.models import Avg, Sum
register = template.Library()

@register.filter(is_safe=True)
def totalise(value):
    return value.id_barang.harga_satuan * value.jumlah

@register.filter(is_safe=True)
def totalShoppingValue(value):
	carts = Keranjang.objects.select_related('id_barang').filter(id_distributor = value.id_dist_id, waktu_belanja = value.id_waktu, status = 'aktif')
	res = 0
	for cart in carts:
		res += cart.id_barang.harga_satuan * cart.jumlah
	return res

@register.filter(is_safe=True)
def jumlahb(value):

	jumlah_barang = Keranjang.objects.filter(id_distributor = value.id_dist_id, waktu_belanja = value.id_waktu, status = 'aktif').aggregate(Sum('jumlah')).get('jumlah__sum')

	return jumlah_barang

@register.filter(is_safe=True)
def Status_user(value):
	online = Session_user.objects.filter(user_id = value.pk)
	cek = online.exists()
	if cek is True:
		on = 'Online'

	else:
		on = 'Offline'

	return on

@register.filter(is_safe=True)
def lacak_user(get):
	Url = Session_user.objects.filter(user_id = get.pk)
	Lacak = Url.first()
	if Url.exists():
		lacak = Lacak.url
	else:
		lacak = 'offline'

	return lacak

@register.filter(is_safe=True)
def barang(value):
	B = Barang.objects.filter(pk = value).first()
	get = B.nm_barang

	return get

@register.filter(is_safe=True)
def convert(val):
	conv = int(val)
	co = str(conv)
	harga = len(co)

	if harga > 3 and harga < 7:

		if harga > 2 and harga < 6:
			Get = co[:1]

		if harga > 4 and harga < 6:
			Get = co[:2]

		elif harga > 5 and harga < 7:
			Get = co[:3]

		wth = 'ribu'
		wtf = Get

	elif harga > 6 and harga < 10:

		if harga > 6 and harga < 8:
			Get = co[:1]
		
		elif harga > 7 and harga < 9:
			Get = co[:2]

		elif harga > 8 and harga < 10:
			Get = co[:3]

		wth = 'juta'
		wtf = Get
	
	holyshit = wtf + wth
	return holyshit