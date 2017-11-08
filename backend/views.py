from django.shortcuts import render, redirect
import datetime
import urllib
import urllib2
import json
import re
import calendar
from backend.web_config import domain
from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpRequest
from django.template import RequestContext
from backend.models import User, Distributor, Session_user, Transaksi, Barang, Keranjang, Fakthur, Settings, Companyprofile, Sale, Contact, Session_user, Contact_reply
from django.core.urlresolvers import reverse
from backend.sessionservice import getUserLogined, getDistributorLogined, webconfig, getlock
from django.db.models import Avg, Sum
from backend.custom_datetime import getdate, getmonth, getyear, gethour
from django.views.generic.edit import FormView
from backend.helper import getcolor, normalize_query, get_query, db_barang, Helper_ObjectRaw
from backend.forms import ContactForm, Petugas, Form_barang, Contact_r, distributor
from django.db.models import Q
from backend.stripe_form import SalePaymentForm



def dashboard(request):
	
	status = getlock(getUserLogined(request.session['nama']))
	if not 'nama' in request.session:
		return redirect('loginpage')
	if status.lock == 1:
		template = 'lock.html'
	else:
		template = 'home.html'
	color = getcolor(7)
	Url = Session_user.objects.filter(user_id=request.session['nama']).update(url=request.path)
	d = Distributor.objects.filter()[:10]
	ym = datetime.datetime.now().strftime("%Y-%m")
	p = Transaksi.objects.filter(waktu_transaksi__icontains = ym)
	count = Transaksi.objects.filter(waktu_transaksi__icontains = ym).count()
	Canvas = Transaksi.objects.all().aggregate(Sum('jumlah_barang')).get('jumlah_barang__sum') or 0
	totalp = Transaksi.objects.filter(waktu_transaksi__icontains = ym).aggregate(Sum('total_pembayaran')).get('total_pembayaran__sum') or 0
	Graphicchart = Transaksi.objects.values('nm_barang').annotate(total=Sum('jumlah_barang')).annotate(totalw=Sum('total_pembayaran')).order_by('nm_barang')
	Helperchart = Transaksi.objects.values('nm_barang').annotate(total=Sum('jumlah_barang')).annotate(totalw=Sum('total_pembayaran')).order_by('-total')
	Helperbarang = Barang.objects.all().order_by('nm_barang')
	Stocksum = Barang.objects.all().aggregate(Sum('stock')).get('stock__sum') or 0
	Laba = 10 * totalp / 100

	year = getyear()
	month = int(getmonth())
	prev_month = month - 1
	if prev_month > 9:
		darurat = ''
	else:
		darurat = 0
	previous_month = '%s-%s%s' % (year, darurat, prev_month)
	tr = Transaksi.objects.filter(waktu_transaksi__icontains=previous_month).aggregate(Sum('total_pembayaran')).get('total_pembayaran__sum') or 0
	getpercent = 100 * Laba/tr

	return render(request, template,{
		'aktif': 'Dashboard',
		'data': getUserLogined(request.session['nama']),
		'users': d,
		'count': count,
		'penjualan': p,
		'bulan': calendar.month_name[month],
		'canvas': Canvas,
		'laba': Laba,
		'total_p': totalp,
		'alert': 'Akun dikunci',
		'percent': getpercent,
		'warna': color,
		'chart': Helperchart,
		'Graphicchart': Graphicchart,
		'Gethelperbarang': Helperbarang,
		'Sumstock' : Stocksum
		})

def loginpage(request):
	if not 'nama' in request.session:
		return render(request,'login.html',{

			'page':'Silahkan login dahulu'

			})
	else:
		return redirect('backend')

def lock_user(request):

	if not 'nama' in request.session:
		return redirect('loginpage')

	if request.method == 'POST':
		ids = getUserLogined(request.session['nama']).pk
		check = Session_user.objects.filter(user_id=ids)
		if check.exists():
			url = request.POST.get('from_url') or 'backend'
			select = User.objects.filter(pk=ids, pswd=request.POST.get('pass'))
			if select.exists():
				Session_user.objects.filter(user_id=ids).update(lock=0)
				return redirect("%s" % url)
			else:
				return render(request, 'lock.html', {
					'alert': 'password salah',
					})
		return render(request, 'lock.html', {
					'alert': 'what the hell r u?'
					})
	else:

		change = Session_user.objects.filter(user_id=getUserLogined(request.session['nama'])).update(lock=1)
		get = getUserLogined(request.session['nama'])
		template = 'lock.html'
		return render(request, template, {
			'data': get
			})

def t_distributor(request):

	status = getlock(getUserLogined(request.session['nama']))
	if not 'nama' in request.session:
		return redirect('loginpage')
	if status.lock == 1:
		template = 'lock.html'
	else:
		template = 'form-distributor.html'
		color = getcolor(7)


	if request.method == 'GET' and 'edit' in request.GET:
			e = request.GET['edit']
			Ambil = Distributor.objects.filter(pk = e)
			if Ambil.exists():
				ambil = Ambil.first()
				return render(request, template, {
					'aktif': 'form-distributor',
					'ambil': ambil,
					'aksi':'edit',
					'data': getUserLogined(request.session['nama']),
					'warna': color,
					'alert': 'Akun dikunci'
				})
			else:
				return render(request, template, {

					'data': getUserLogined(request.session['nama']),
					'aksi': 'tidak ditemukan',
					'warna': color

					})
	else:
			return render(request, template, {
				'aktif': 'form distributor',
				'aksi':'Tambah',
				'data': getUserLogined(request.session['nama']),
				'aktif': 'Tambah distributor',
				'warna': color,
				'alert': 'Akun dikunci'
			})
def data_distributor(request):

	status = getlock(getUserLogined(request.session['nama']))
	if not 'nama' in request.session:
		return redirect('loginpage')
	if status.lock == 1:
		template = 'lock.html'
	else:
		template = 'data-distributor.html'

	if request.method == 'GET' and 'edit' in request.GET:
		act = 'edit data distributor'
	else:
		act = 'data distributor'

	color = getcolor(7)
	Url = Session_user.objects.filter(user_id=request.session['nama']).update(url=request.path)
	data = Distributor.objects.filter()
	return render(request, template, {
		'aktif': act,
		'dist':data,
		'data': getUserLogined(request.session['nama']),
		'warna': color,
		'alert': 'Akun dikunci'

		})

def data_penjualan(request):

	status = getlock(getUserLogined(request.session['nama']))
	if not 'nama' in request.session:
		return redirect('loginpage')
	if status.lock == 1:
		template = 'lock.html'
	else:
		template = 'data-penjualan.html'

	color = getcolor(7)
	Url = Session_user.objects.filter(user_id=request.session['nama']).update(url=request.path)
	data = Transaksi.objects.select_related('id_dist').order_by('-pk')
	return render(request, template, {
		'aktif': 'data penjualan',
		'penjualan': data,
		'data': getUserLogined(request.session['nama']),
		'warna': color,
		'alert': 'Akun dikunci'
		})

def data_petugas(request):

	status = getlock(getUserLogined(request.session['nama']))
	if not 'nama' in request.session:
		return redirect('loginpage')
	if status.lock == 1:
		template = 'lock.html'
		alert = 'Akun dikunci'
	else:
		template = 'data-petugas.html'
		
	if request.method == 'GET' and 'edit' in request.GET:
		act = 'edit data petugas'
		alert = 0

	elif request.method == 'GET' and 'delete' in request.GET:
		User.objects.filter(pk=request.GET['delete']).delete()
		alert = 'Berhasil dihapus'
		act = 'data petugas'
	elif request.method == 'GET' and 'added' in request.GET:
		alert = 'Berhasil diperbaruhi'
		act = 'data petugas'

	else:
		act = 'data petugas'
		alert = 0
	color = getcolor(7)
	Url = Session_user.objects.filter(user_id=request.session['nama']).update(url=request.path)
	return render(request, template, {
		'aktif': act,
		'datap': User.objects.filter(),
		'data': getUserLogined(request.session['nama']),
		'warna': color,
		'alert': alert
		
		})

def f_petugas(request):
	
	if not 'nama' in request.session:
		return redirect(reverse('login'))
	else:
		color = getcolor(7)
		Url = Session_user.objects.filter(user_id=request.session['nama']).update(url=request.path)
		if request.method == 'POST':

			form = Petugas(data=request.POST)
			recaptcha_response = request.POST.get('g-recaptcha-response')
			url = 'https://www.google.com/recaptcha/api/siteverify'
			values = {
				'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
				'response': recaptcha_response
			}
			data = urllib.urlencode(values)
			req = urllib2.Request(url, data)
			response = urllib2.urlopen(req)
			result = json.load(response)

			if result['success']:
				idf = form.save(commit=False)

				if request.POST.get('idk') != '0':
					idf.pk = request.POST.get('idk')
				idf.save()

				return redirect("%sdata-petugas/?updated" % domain())

			else:
				return render(request, 'form-petugas.html', {

					'confirm': 'Chaptca salah'

					})

		elif request.method == 'GET' and 'id' in request.GET:
			form = Petugas(instance = User.objects.get(pk = request.GET['id']))
			aksi = 'edit'
			aktif = 'edit petugas'
			idk = request.GET['id']
		else:
			form = Petugas()
			aksi = 'tambah'
			aktif = 'tambah petugas'
			idk = 0
		return render(request, 'form-petugas.html', {
			'aktif': aktif,
			'data': getUserLogined(request.session['nama']),
			'form': form,
			'aksi': aksi,
			'warna': color,
			'get_id': idk
			})

def index_page(request):

	conf = webconfig(1)
	color = getcolor(7)
	if conf.config == 'on':
		template = 'error.html'
	else:
		template = 'index.html'

	Anggota = Distributor.objects.all().order_by('-pk')[:5]
	ym = datetime.datetime.now().strftime("%Y-%m")
	barang = Barang.objects.filter() 
	r = Transaksi.objects.filter(waktu_transaksi__icontains = ym).aggregate(Sum('total_pembayaran')).get('total_pembayaran__sum') or 0
	R = 10 * r / 100
	return render(request, template, {

		'barang': barang,
		'page': 'Shemura MT',
		'rata_rata': R,
		'alert': 'UnderMaintenance',
		'anggota': Anggota,
		'today': datetime.datetime.now(),
		'warna': color

		})

def tentang_kami(request):

	color = getcolor(7)
	Post = Companyprofile.objects.filter(pk=1)
	post = Post.first()

	return render(request, 'tentang-kami.html', {'mt':post, 'page': 'Tentang kami', 'warna': color})


def keranjang(request):

	if not 'id' in request.session:
		return redirect('%slogin-distributor/?d' % domain())
	else:
		color = getcolor(7)
		conf = webconfig(2)
		if request.method == 'GET' and 'server-reply' in request.GET:
			if request.GET['server-reply'] == 'keranjang-penuh':
				Reply = 'Keranjang penuh, Selesaikan transaksi anda sebelumnya atau hapus transaksi aktif sebelumnya'
			elif request.GET['server-reply'] == 'keranjang-kosong':
				Reply = 'Keranjang kosong, Selesaikan masukkan barang ke keranjang'
		else:
			Reply = 'Keranjang'

		if conf.config == 'on':
			template = 'error.html'

		else:
			template = 'keranjang.html'
			
		
		idk = getDistributorLogined(request.session['id']).pk
		
		K = Keranjang.objects.select_related('id_barang').filter(id_distributor = idk, status='tidak_aktif')
		tot = 0
		for barang in K:
			tot += barang.id_barang.harga_satuan * barang.jumlah

		return render(request, template, {
			'idb': getDistributorLogined(request.session['id']),
			'keranjang': K,
			'page': 'Keranjang',
			'total': tot,
			'reply': Reply,
			'alert': 'Sold out',
			'warna': color
			})

def profil_distributor(request):

	conf = webconfig(1)
	
	if conf.config == 'on':
		template = 'error.html'

	else:
		template = 'profil-distributor.html'

	if request.method == 'POST':
		update = distributor(data = request.POST)
		up = update.save(commit=False)
		up.pk = request.session['id']
		up.save()
		return redirect('%sdistributor/?updated' % domain())

	if not 'id' in request.session:
		return redirect('%slogin-distributor/?d' % domain())
	color = getcolor(7)
	form = distributor(instance = Distributor.objects.get(pk = getDistributorLogined(request.session['id']).pk))
	tr = Fakthur.objects.filter(id_dist = getDistributorLogined(request.session['id']).pk).order_by('pk') 
	Gtr = Transaksi.objects.filter(id_dist = getDistributorLogined(request.session['id']).pk).order_by('-waktu_transaksi')[:3]
	Gttr = Transaksi.objects.filter(id_dist = getDistributorLogined(request.session['id']).pk).order_by('harga')
	total_p = Transaksi.objects.filter(id_dist = getDistributorLogined(request.session['id']).pk).aggregate(Sum('total_pembayaran')).get('total_pembayaran__sum') or 0
	countb = Gttr.count()
	transaksi_gagal = getDistributorLogined(request.session['id']).j_transaksi or 0 - countb
	return render(request, template, {
		'ambil': getDistributorLogined(request.session['id']),
		'tr': tr,
		'gettr': Gttr,
		'page': 'Profile',
		'gtr': Gtr,
		'alert': 'UnderMaintenance',
		'tp': total_p,
		'count': Gttr.count(),
		'Tb': transaksi_gagal,
		'warna': color,
		'form': form
		})

def login_d(request):
	color = getcolor(7)
	if not 'id' in request.session:
		return render(request, 'login-distributor.html', {
			'page': 'Login',
			'warna': color
			})
	else:	
		return redirect(reverse('p_distributor'))

def pemesanan(request):
	color = getcolor(7)
	if request.method == 'GET' and 'id' in request.GET:
		id_barang = request.GET['id']
		order = Barang.objects.filter(pk = id_barang)
		if order.exists():
			barang = order.first()
			return render(request, 'pemesanan.html', {

				'barang': barang,
				'page': barang.nm_barang,
				'warna': color,
				'db_barang': db_barang(6)

				})
		else:
			return render(request, 'pemesanan.html', {

				'alert': 'Barang tidak ditemukan',
				'warna': color

				})
	else:		
		return render(request, 'pemesanan.html', {

			'alert': 'Silahkan pilih barang yang ingin dipesan',
			'warna': color

			})

def fakthur_p(request):

	if not 'id' in request.session:
		return redirect(reverse('login_distributor'))
	
	else:
		color = getcolor(7)
		if request.method == "POST":
			form = SalePaymentForm(request.POST)
	 
			if form.is_valid(): 
				return HttpResponse("Success! We ve charged your card!")

		if request.method == 'GET' and 'id' in request.GET:
			if request.GET['id'] != '':
				id_f = request.GET['id']
				hg = getDistributorLogined(request.session['id']).pk
				idg = Fakthur.objects.filter(pk=id_f, id_dist=hg)
				if idg.exists():	
					conf = webconfig(6)
					conf2 = webconfig(5)
					idf = idg.first()
					dst = Keranjang.objects.select_related('id_barang').filter(id_distributor = idf.id_dist_id, waktu_belanja = idf.id_waktu, status='aktif')
					if dst.exists():

						form = SalePaymentForm()

						tot = 0
						for dt in dst:
							tot += dt.jumlah * dt.id_barang.harga_satuan	
						return render(request, 'fakthur-pemesanan.html', {

							'ambil': getDistributorLogined(request.session['id']),
							'sub_total': tot,
							'fakthur': dst,
							'pesan': 'sukses',
							'page': 'Faktur Pemesanan',
							'dd': idf,
							'form': form,
							'conf': conf,
							'warna': color,
							'conf2':conf2

							})
					else:
						return render(request, 'fakthur-pemesanan.html', {
							'pesan': '404',
							'alert': '500',
							'warna': color
							})
				else:
					return render(request, 'fakthur-pemesanan.html', {
							'pesan': '404',
							'alert': 'WTF',
							'warna': color
							})
			else:
				return render(request, 'fakthur-pemesanan.html', {
						'pesan': '404',
						'alert': 'id kosong',
						'warna': color
						})

		else:
			return render(request, 'fakthur-pemesanan.html', {
						'pesan': '404',
						'alert':'404',
						'warna': color

						})

def hub_kami(request):
	color = getcolor(7)
	if 'id' in request.session:

		form = ContactForm(instance=Distributor.objects.get(pk = request.session.get('id')))
		gt = getDistributorLogined(request.session['id'])
		
	elif not 'id' in request.session:
		form = ContactForm()
		gt = 0

	if request.method == 'POST':
		form = ContactForm(request.POST)
		recaptcha_response = request.POST.get('g-recaptcha-response')
		url = 'https://www.google.com/recaptcha/api/siteverify'
		values = {
			'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
			'response': recaptcha_response
		}
		data = urllib.urlencode(values)
		req = urllib2.Request(url, data)
		response = urllib2.urlopen(req)
		result = json.load(response)

		if result['success']:
			new_form = form.save(commit=False)
			new_form.distributor_id = request.POST.get('id_d')
			new_form.save()
			confirm = 'Pesan berhasil dikirim ke database kami silahkan tunggu balasan email dari kami secepatnya'

		else:
			confirm = 'Captcha salah'

		return render(request, "hubungi-kami.html", {
			'form': form,
			'gt': gt, 
			'page': 'Hubungi kami',
			'warna': color,
			'confirm' : confirm
			
			})



	return render(request, "hubungi-kami.html", {
		'form': form,
		'gt': gt, 
		'page': 'Hubungi kami',
		'warna': color
		
		})

def t_aktif(request):
	color = getcolor(7)
	tr = Fakthur.objects.select_related('id_dist').all()
	template = 'transaksi-aktif.html'

	return render(request, template, {
		'get':tr,
		'data': getUserLogined(request.session['nama']),
		'aktif':'transaksi aktif',
		'warna': color

		})

def pbarang(request):

	status = getlock(getUserLogined(request.session['nama']))
	if not 'nama' in request.session:
		return redirect('loginpage')
	if status.lock == 1:
		template = 'lock.html'

	else:
		template = 'pbarang.html'

	if request.method == 'GET' and 'success' in request.GET:
		Transaksi.objects.filter(pk=request.GET['success']).update(status=1)
		sukses = 1
	else:
		sukses = 0

	color = getcolor(7)
	Url = Session_user.objects.filter(user_id=request.session['nama']).update(url=request.path)
	data = Transaksi.objects.select_related('id_dist').filter(status=0)
	return render(request, template, {
		'aktif': 'pengiriman barang',
		'penjualan': data,
		'data': getUserLogined(request.session['nama']),
		'warna': color,
		'alert': 'Akun dikunci',
		'pesan': sukses
		})



def email(request):

	if not 'nama' in request.session:
		return redirect(reverse('login_distributor'))
	
	else:
		if request.method == 'GET' and 'mail' in request.GET:
			G = Contact.objects.select_related('distributor').filter(pk = request.GET['mail'])
			Get = G.first()

		elif request.method == "POST":
			form = Contact_r(request.POST)
			recaptcha_response = request.POST.get('g-recaptcha-response')
			url = 'https://www.google.com/recaptcha/api/siteverify'
			values = {
				'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
				'response': recaptcha_response
			}
			data = urllib.urlencode(values)
			req = urllib2.Request(url, data)
			response = urllib2.urlopen(req)
			result = json.load(response)

			if result['success']:
				form.contact_id = request.POST.get('cid')
				balas = form.save()
				return redirect('mail')
				send_mail('Subject here', 'Here is the message.', 'admin@hexca.com', ['arnoldfox21@gmail.com'], fail_silently=False)

		else:
			G = 0
			Get = 0
		color = getcolor(7)
		template = 'email.html'
		reply = Contact_r()

		daft = Contact.objects.select_related('distributor').order_by('-pk')[:8]
		F = daft.first()
		return render(request, template, {
			'data': getUserLogined(request.session['nama']),
			'aktif': 'email',
			'f': F,
			'daft': daft,
			'g': G,
			'get': Get,
			'form_r': reply,
			'warna': color
			})


def hub_suplier(request):

	if not 'nama' in request.session:
		return redirect('loginpage')
	else:
		color = getcolor(7)
		if request.method == 'GET' and 'code' in request.GET:
			Status = request.GET['code']
		elif not 'code' in request.GET:
			Status = 'ok'

		template = 'form-ps.html'
		Url = Session_user.objects.filter(user_id=request.session['nama']).update(url=request.path)
		return render(request, template, {
			'data': getUserLogined(request.session['nama']),
			'aktif': 'fps',
			'status': Status,
			'warna': color
			})

def data_barang(request):
	color = getcolor(7)
	template = 'data-barang.html'
	Url = Session_user.objects.filter(user_id=request.session['nama']).update(url=request.path)
	db = Barang.objects.all()

	if request.method == 'GET' and 'edit' in request.GET:
		act = 'edit data barang'

	elif request.method == 'GET' and 'delete' in request.GET:
		hapus = Barang.objects.filter(pk=request.GET['delete']).first()
		act = '%s Berhasil dihapus' % (hapus.nm_barang)
		hapus.delete()
	else:
		act = 'data barang'

	return render(request, template, {
		'aktif': act,
		'data': getUserLogined(request.session['nama']),
		'dbg': db,
		'warna': color
		})


def charge(request):
	if request.method == "POST":
		form = SalePaymentForm(request.POST)
 
		if form.is_valid(): 
			return HttpResponse("Success! We ve charged your card!")
	else:

		form = SalePaymentForm()
 
	return render(request, "fakthur-pemesanan.html", {'form': form})

def f_barang(request):

	if not 'nama' in request.session:
		return redirect(reverse('login'))
	else:
		color = getcolor(7)
		if request.method == 'POST':
			form = Form_barang(data=request.POST)
			recaptcha_response = request.POST.get('g-recaptcha-response')
			url = 'https://www.google.com/recaptcha/api/siteverify'
			values = {
				'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
				'response': recaptcha_response
			}
			data = urllib.urlencode(values)
			req = urllib2.Request(url, data)
			response = urllib2.urlopen(req)
			result = json.load(response)

			if result['success']:
				simpan = form.save(commit=False)
				if request.POST.get('idb'):
					simpan.pk = request.POST.get('idb')

				simpan.save()
				return redirect('%sdata-barang/?edit&updated' % domain())
			
			else:
				getid = request.POST.get('idb')	
				if getid:
					
					return redirect('%sform-barang/?edit=%s&error-captcha' % (domain(), getid))
				else:

					return redirect('%sform-barang/?error-captcha' % domain())
					

		elif request.method == 'GET' and 'edit' in request.GET:
			form = Form_barang(instance = Barang.objects.get(pk = request.GET['edit']))
			aksi = 'edit'
			edit = request.GET['edit']
		else:
			form = Form_barang()
			aksi = 'tambah'
			edit = 0
		return render(request, 'form-barang.html', {
			'id': edit,
			'aktif': aksi + ' barang',
			'data': getUserLogined(request.session['nama']),
			'form': form,
			'aksi': aksi,
			'warna': color
			})

def setting(request):
	
	if not 'nama' in request.session:
		return redirect('loginpage')

	color = getcolor(7)
	get = Settings.objects.all().order_by('pk')[:5]
	return render(request, 'settings.html', {
		'data': getUserLogined(request.session['nama']),
		'Setting': get,
		'aktif': 'web settings',
		'warna': color
		})

def handler404(request):
	return render(request, 'error.html', status=404)

def handler500(request):
	return render(request, 'error.html', status=500)

def detail(request):
	color = getcolor(7)
	template = 'detail.html'
	if not 'nama' in request.session:
		return redirect('loginpage')
	if request.method == 'GET' and not 'id' in request.GET:
		go = 'Page not found'
	else:
		if request.method == 'POST':
			form = Contact_r(request.POST)
			new_form = form.save(commit=False)
			new_form.customer_id = request.POST.get('ci_d')
			new_form.save()
		form_r = Contact_r()
		d = Distributor.objects.filter(pk=request.GET['id'])
		if d.exists():
			go = d.first()
			data_t = Transaksi.objects.select_related('id_dist').filter(id_dist=go.pk).order_by('-pk')
			count = data_t.count()
			fcount = Transaksi.objects.filter(id_dist_id=d).aggregate(Sum('total_pembayaran')).get('total_pembayaran__sum') or 0	
			fcountb = Transaksi.objects.filter(id_dist_id=d).aggregate(Sum('jumlah_barang')).get('jumlah_barang__sum') or 0			
			border = Settings.objects.filter(pk= 7).first()
		else:
			go = 'id tidak ditemukan'
	return render(request, template, {
		'warna': color,
		'data': getUserLogined(request.session['nama']),
		'aktif': 'detail',
		'fdata': go,
		'd_t': data_t,
		'count': count,
		'form_r': form_r,
		'border': border,
		'fcount': fcount,
		'fcountb': fcountb
		})

def search_for_something(request):

	color = getcolor(7)
	query_string = ''
	temukan = None

	if ('q' in request.GET) and request.GET['q'].strip():
		query_string = request.GET['q']
		entry_query = get_query(query_string, ['id', 'nama', 'alamat', 'umail'])
		barang = get_query(query_string, ['id', 'nm_barang'])
		user = get_query(query_string, ['id', 'username', 'jabatan', 'umail'])
		transaksi = get_query(query_string, ['id', 'nm_barang','total_pembayaran'])
		temukan_d = Distributor.objects.filter(entry_query).order_by('pk')
		temukan_b = Barang.objects.filter(barang).order_by('pk')
		temukan_t = Transaksi.objects.select_related('id_dist').filter(transaksi).order_by('pk')
		temukan_u = User.objects.filter(user).order_by('pk')

	return render(request, 'result.html',{ 

		'data': getUserLogined(request.session['nama']), 
		'query_string': query_string, 
		'found_entries': temukan_d, 
		'barang': temukan_b,
		'transaksi': temukan_t,
		'user': temukan_u,
		'warna': color 

		})

