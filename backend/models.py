from django.db import models

from django.conf import settings


class User(models.Model):
	
	username = models.CharField(max_length = 50, null = True)
	pswd = models.CharField(max_length = 50, null = True)
	umail = models.CharField(max_length = 200, null= True)
	jabatan = models.CharField(max_length = 200, null=True)

class Distributor(models.Model):

	nama = models.CharField(max_length = 200, null= True)
	pswd = models.CharField(max_length = 200, null= True)
	umail = models.CharField(max_length= 200, null= True, default="")
	alamat = models.CharField(max_length = 200, null= True)
	tgl_lahir = models.CharField(max_length = 200, null=True)
	jenis_kelamin = models.CharField(max_length = 1, null=True)
	telp = models.CharField(max_length = 200, null=True)
	foto = models.CharField(max_length = 200, null=True)
	joined_time = models.CharField(max_length = 20, null=True)
	j_transaksi = models.IntegerField(null=True)
	status = models.CharField(max_length=20, null=True)

class Transaksi(models.Model):

	waktu_transaksi = models.CharField(max_length = 200, null= True)
	nm_barang = models.CharField(max_length = 200, null=True)
	harga = models.IntegerField(null=True)
	id_dist = models.ForeignKey(Distributor, null=True)
	jumlah_barang = models.IntegerField(null=True)
	total_pembayaran = models.IntegerField(null=True)
	status = models.IntegerField(null=True)

class Barang(models.Model):

	nm_barang = models.CharField(max_length = 200, null=True)
	harga_satuan = models.IntegerField(null=True)
	stock = models.IntegerField(null=True)
	berat = models.CharField(max_length = 200, null=True)
	warna = models.CharField(max_length = 200, null=True)
	ket_tambahan = models.CharField(max_length = 200, null=True)

class Keranjang(models.Model):

	id_distributor = models.IntegerField(null = True)
	id_barang = models.ForeignKey(Barang, null=True)
	waktu_belanja = models.CharField(max_length = 200, null=True)
	jumlah = models.IntegerField(null=True)
	status = models.CharField(max_length = 200, null=True)

class Contact(models.Model):
	
	distributor = models.ForeignKey(Distributor, null=True)
	nama = models.CharField(max_length= 200, null=True)
	umail = models.CharField(max_length= 200, null=True)
	web = models.CharField(max_length= 200, null=True)
	pesan = models.CharField(max_length=200, null=True)
	subject = models.CharField(max_length=200, null=True)

class Fakthur(models.Model):

	id_dist = models.ForeignKey(Distributor, Keranjang, null=True)
	id_waktu = models.CharField(max_length=200)

class Bahan(models.Model):

	nama_bahan = models.CharField(max_length=200, null=True)
	stock = models.IntegerField(null=True)

class Companyprofile(models.Model):
	
	title = models.CharField(max_length=200)
	description = models.CharField(max_length=2000)
	about_title = models.CharField(max_length=200)
	about_post = models.TextField()
		
class Session_distributor(models.Model):

	distributor = models.ForeignKey(Distributor)
	start_time = models.CharField(max_length= 20)
	url = models.CharField(max_length=200)

class Session_user(models.Model):
	
	user = models.ForeignKey(User)
	start_time = models.CharField(max_length= 200)
	url = models.CharField(max_length=200, null=True)
 	lock = models.IntegerField(null=True)

class Sale(models.Model):
	
	def __init__(self, *args, **kwargs):
		super(Sale, self).__init__(*args, **kwargs)
		import stripe

		stripe.api_key = settings.STRIPE_API_KEY
		self.stripe = stripe
		
	charge_id = models.CharField(max_length=32)
 
	def charge(self, price_in_cents, number, exp_month, exp_year, cvc):

		if self.charge_id:
				return False, Exception(message="Already charged.")
		try:
			response = self.stripe.Charge.create(
				amount = price_in_cents,
				currency = "usd",
				card = {
					"number" : number,
					"exp_month" : exp_month,
					"exp_year" : exp_year,
					"cvc" : cvc,
				},
				description='Thank you for your purchase!')
			self.charge_id = response.id
 
		except self.stripe.CardError, ce:
			return False, ce

		return True, response

class Contact_reply(models.Model):

	customer = models.ForeignKey(Distributor, null=True)
	contact = models.ForeignKey(Contact, null=True)
	pesan = models.CharField(max_length=1000, null=True)

class Settings(models.Model):

	setting = models.CharField(max_length=200, null=True)
	config = models.CharField(max_length=200, null=True)
	info = models.CharField(max_length=300, null=True)