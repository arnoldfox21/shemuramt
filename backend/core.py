from django.shortcuts import render, redirect
import urllib
import urllib2
import json

from backend.web_config import domain
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template import RequestContext
from backend.models import User, Distributor, Keranjang, Contact, Fakthur, Transaksi, Barang, Settings, Session_distributor, Session_user
from backend.sessionservice import getUserLogined, getDistributorLogined
from backend.helper import getcolor
from django.core.urlresolvers import reverse
from django.conf import settings
import datetime
from django.core.files.storage import FileSystemStorage

def h_dist(request):

	if request.method == 'POST' and 'foto_profil' in request.GET:
		myfile = request.FILES['foto_profil']
		get_id = getDistributorLogined(request.session['id']).pk
		name = getDistributorLogined(request.session['id']).nama
		get_name = name.replace(" ","_")
		get_ext = myfile.name.split('.')[-1]
		rename = str(get_name) + "_" + str(get_id) + "." + str(get_ext)
		Distributor.objects.filter(pk= get_id).update(foto=rename)
		fs = FileSystemStorage()
		fs.delete(getDistributorLogined(request.session['id']).foto)
		filename = fs.save(rename, myfile)
		uploaded_file_url = fs.url(filename)
		return redirect('%sdistributor/?updated' % domain())

	elif request.method == 'GET' and 'delete' in request.GET:
		q = request.GET['delete']
		hapus = Distributor.objects.filter(pk = q).delete()	
		return redirect(reverse('d_distributor'))

	elif request.method == 'GET' and 'update_status' in request.GET:
		Distributor.objects.filter(pk=request.GET['id']).update(status=request.GET['update_status'])
		return redirect('%sdetail-distributor?id=%s' % (domain(), request.GET['id']))

	elif request.method == 'POST' and 'request_setting' in request.GET:

		if request.method == 'POST':
			
			mw = request.POST.get('1', None)
			Settings.objects.filter(pk=1).update(config=mw)
			mpt = request.POST.get('2', None)
			Settings.objects.filter(pk=2).update(config=mpt)
			sl = request.POST.get('4', None)
			Settings.objects.filter(pk=4).update(config=sl)
			bt = request.POST.get('5', None)
			Settings.objects.filter(pk=5).update(config=bt)
			pkk = request.POST.get('6', None)
			Settings.objects.filter(pk=6).update(config=pkk)
			warna = request.POST.get('color', None)
			Settings.objects.filter(pk=7).update(config=warna)

			return redirect('%ssettings/?updated' % domain())

		else:
			return redirect('setting')


	elif request.method == 'POST' and 'update' in request.GET:
		add = Distributor()
		if request.POST.get('idd') != '':
			add.pk = request.POST.get('idd')
		add.nama = request.POST.get('nama', None)
		add.umail = request.POST.get('umail', None)
		add.pswd = request.POST.get('password', None)
		add.jenis_kelamin = request.POST.get('jk', None)
		add.tgl_lahir = request.POST.get('tgl_l', None)
		add.telp = request.POST.get('telp', None)
		add.alamat = request.POST.get('alamat', None)
		add.save()
		if add:
			return redirect("%sdata-distributor/?updated" % domain())

		else:
			return render(request, 'form-distributor.html', {

				'pesan': 'GAGAL MENAMBAHKAN'
				
				})
	elif request.method == 'GET' and 'hapus-keranjang' in request.GET:
		hapus = Keranjang.objects.filter(id = request.GET['hapus-keranjang']).delete()
		if hapus:
			return redirect('keranjang')

		else:
			return redirect('profil')

	elif request.method == 'GET' and 'd_transaksi' in request.GET:
	
		Getid = Fakthur.objects.filter(pk = request.GET['d_transaksi'], id_dist=getDistributorLogined(request.session['id']).pk)
		if Getid.exists():
			getid = Getid.first()
			Keranjang.objects.filter(id_distributor = getDistributorLogined(request.session['id']).pk, waktu_belanja = getid.id_waktu, status='aktif').delete()
			Getid.delete()
			return redirect('p_distributor')
		else:
			return redirect('p_distributor')

	elif request.method == 'GET' and 'verifikasi' in request.GET:
		
		if not 'nama' in request.session:
			return redirect('index')
		else:
			Getid = Fakthur.objects.filter(pk = request.GET['verifikasi'])
			if Getid.exists():
				getid = Getid.first()
				K = Keranjang.objects.filter(waktu_belanja = getid.id_waktu, status='aktif', id_distributor=getid.id_dist_id)
				ready = Keranjang.objects.select_related('id_barang').filter(id_distributor = getid.id_dist_id, waktu_belanja = getid.id_waktu, status='aktif')
				Ready = ready.first()

				barang = Ready.id_barang
				barang.stock -= Ready.jumlah
				barang.save()
				
				for keranjang in ready:
					insert = Transaksi()
					insert.nm_barang = keranjang.id_barang.nm_barang
					insert.waktu_transaksi = getid.id_waktu
					insert.harga = keranjang.id_barang.harga_satuan
					insert.id_dist = getid.id_dist
					insert.jumlah_barang = keranjang.jumlah
					insert.total_pembayaran = keranjang.jumlah * keranjang.id_barang.harga_satuan
					insert.status = 0
					insert.save()

				Getid.delete()
				K.delete()
				return redirect('%stransaksi-aktif/?verified' % domain())
			else:
				return redirect('t_aktif')

	elif request.method == 'GET' and 'hapus-transaksi' in request.GET:
		
		if not 'nama' in request.session:
			return redirect('index')
		else:
			Getid = Fakthur.objects.filter(pk = request.GET['hapus-transaksi'])
			if Getid.exists():
				getid = Getid.first()
				K = Keranjang.objects.filter(waktu_belanja = getid.id_waktu, status='aktif', id_distributor=getid.id_dist_id)
				Getid.delete()
				K.delete()
				return redirect('%stransaksi-aktif/?deleted' % domain())
			else:
				return redirect('t_aktif')



def humanizeTimeDiff(timestamp = None):

	timeDiff = datetime.datetime.now() - timestamp
	days = timeDiff.days
	hours = timeDiff.seconds/3600
	minutes = timeDiff.seconds%3600/60
	seconds = timeDiff.seconds%3600%60

	str = ""
	tStr = ""
	if days > 0:
		if days == 1:   tStr = "day"
		else:           tStr = "days"
		str = str + "%s %s" %(days, tStr)
		return str
	elif hours > 0:
		if hours == 1:  tStr = "hour"
		else:           tStr = "hours"
		str = str + "%s %s" %(hours, tStr)
		return str
	elif minutes > 0:
		if minutes == 1:tStr = "min"
		else:           tStr = "mins"           
		str = str + "%s %s" %(minutes, tStr)
		return str
	elif seconds > 0:
		if seconds == 1:tStr = "sec"
		else:           tStr = "secs"
		str = str + "%s %s" %(seconds, tStr)
		return str
	else:
		return None

	
def login(request):

	if request.method == "POST":
		uname = User.objects.filter(umail = request.POST.get('mail', None), pswd = request.POST.get('password', None))
		if uname.exists():
			uname = uname.first()

			insert = Session_user()
			insert.user_id = uname.pk
			insert.url = request.path
			insert.start_time = datetime.datetime.now()
			insert.save()

			request.session['nama'] = uname.pk
			return redirect(reverse('backend'))

		else:
			return render(request, 'login.html', {
				'pesan': 'Email atau password salah'

				})

	else:
		return redirect('loginpage')


def logout(request):
	d = Session_user.objects.filter(user_id = request.session['nama'])
	d.delete()
	del request.session['nama']
	return redirect('loginpage')

def login_validasi_dist(request):

	user = Distributor.objects.filter(umail = request.POST.get('umail', None), pswd = request.POST.get('pswd', None))
	color = getcolor(7)
	if user.exists():
		ref = request.POST.get('from_url') or 'p_distributor'
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
			nama = user.first()

			request.session['id'] = nama.pk
			return redirect("%s" % ref)

		else:
			return render(request, 'login-distributor.html', { 
				'pesan': 'captcha salah',
				'warna': color,
				'page': 'Login',
			 })
	
	else:
		return render(request, 'login-distributor.html', {
			'pesan': 'Email atau password salah',
			'warna': color,
			'page': 'Login',
			})

def logout_d(request):
	del request.session['id']
	return redirect(reverse('login_distributor'))

def add_chart(request):
	
	if not 'id' in request.session:
		return redirect('%slogin-distributor/?d' % domain())
	
	else:
		idb = request.POST.get('id_barang')
		cek = Barang.objects.filter(pk=idb)
		if cek.exists():
			tambah = Keranjang()
			tambah.id_distributor = getDistributorLogined(request.session['id']).pk
			tambah.id_barang_id = idb
			tambah.jumlah = request.POST.get('jumlah')
			tambah.status = 'tidak_aktif'
			yakin = tambah.save()
			return redirect(reverse('keranjang'))
		else:
			return redirect(reverse('keranjang'))

def cetak_fakthur(request):
	
	if 'id' in request.session:
		wib = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
		idd = getDistributorLogined(request.session['id'])
		cek = Fakthur.objects.filter(id_dist = idd).count()
		cek_k = Keranjang.objects.filter(id_distributor=idd.pk, status='tidak_aktif').exists()
		if cek_k is False:

			return redirect("keranjang/?server-reply=keranjang-kosong")
		elif cek > 2:

			return redirect("keranjang/?server-reply=keranjang-penuh")
		else:
			tambah = Fakthur()
			tambah.id_dist = idd
			tambah.id_waktu = wib
			tambahkan = tambah.save()

			Keranjang.objects.filter(id_distributor=idd.pk, status='tidak_aktif').update(waktu_belanja=wib, status='aktif')
			# Distributor.objects.filter(pk=idd).update(j_transaksi= +1)
			getid = Fakthur.objects.filter(id_dist=idd, id_waktu=wib)
			Getid = getid.first()

			return redirect("fakthur-pemesanan/?id=%s" % Getid.pk)
	else:
		return redirect('index')

