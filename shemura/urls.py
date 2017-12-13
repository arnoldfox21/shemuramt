"""shemura URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from backend.views import dashboard, data_suplier, form_suplier, forgot_pass, data_pembelian, charge, hub_suplier, detail, lock_user, pbarang, search_for_something, f_petugas, setting, data_barang, loginpage, index_page, handler500, handler404, f_barang, t_distributor, email, data_distributor, data_petugas, data_penjualan, tentang_kami, keranjang, profil_distributor, login_d, fakthur_p, hub_kami, pemesanan, t_aktif
from backend.core import h_dist, login, login_validasi_dist, logout, logout_d, add_chart, cetak_fakthur 
from backend.api_views import (ReadUser, RegisterUser, UpdateUser)
from backend.api.APIdistributor import (SelectAllDistributor, loginview)
from backend.api.APIsupplier import (OrderBahan)
from backend.api.APIbarang import (Selectitem, SelectAll)


urlpatterns = [
    url(r'^admin/$',  dashboard, name='backend'),
    url(r'^developer/',  include(admin.site.urls)),
    url(r'^login/$', loginpage, name='loginpage'),
    url(r'^cek/$', login, name='cek'),
    url(r'^logout/$', logout, name='logout'),
    url(r'^hdist/$', h_dist, name='h_t'),
    url(r'^data-distributor/$', data_distributor, name='d_distributor'),
    url(r'^form-distributor/$', t_distributor, name='t_distributor'),
    url(r'^data-petugas/$', data_petugas, name='data-petugas'),
    url(r'^data-penjualan/$', data_penjualan, name='d_penjualan'),
    url(r'^$', index_page, name='index'),
    url(r'^lock/$', lock_user, name='lock'),
    url(r'^tentang-kami/$', tentang_kami, name='tentangkami'),
    url(r'^hubungi-kami/$', hub_kami, name='hub_kami'),
    url(r'^keranjang/$', keranjang, name='keranjang'),
    url(r'^distributor/$', profil_distributor, name='p_distributor'),
    url(r'^login-distributor/$', login_d, name='login_distributor'),
    url(r'^validasi-login/$', login_validasi_dist, name='validasi-login-distributor'),
    url(r'^logout-d/$', logout_d, name='logout_d'),
    url(r'^fakthur-pemesanan/$', fakthur_p, name='fakthur-pemesanan'),
    url(r'^pemesanan', pemesanan, name='pemesanan'),
    url(r'^tambah-ke-keranjang', add_chart, name='add_chart'),
    url(r'cetak', cetak_fakthur, name='ck'),
    url(r'^transaksi-aktif/$', t_aktif, name='t_aktif'),
    url(r'^pengiriman-barang/$', pbarang, name='pbarang'),
    url(r'^email/$', email, name='mail'),
    url(r'^form-pemesanan-suplier/$', hub_suplier, name='fps'),
    url(r'^data-barang/$', data_barang, name='dbarang'),
    url(r'^charge/$', charge, name="charge"),
    url(r'^form-petugas/$', f_petugas, name='f_petugas'),
    url(r'^form-barang/$', f_barang, name='f_barang'),
    url(r'^settings/$', setting, name='setting'),
    url(r'^results/$', search_for_something, name='search_for_something'),
    url(r'^detail-distributor$', detail, name="detail_d"),
    url(r'^data-pembelian$', data_pembelian, name="d_pembelian"),
    url(r'^forgot-password$', forgot_pass, name= 'forgot-password'),
    url(r'^data-suplier$', data_suplier, name='data-suplier'),
    url(r'^fsuplier$', form_suplier, name='fes'),
    url(r'^handler404/$', handler404),
    url(r'^handler500/$', handler500),

    url(r'^orderb/$', OrderBahan.as_view(), name='orderb'),
    url(r'^barang/select/$', Selectitem.as_view(), name='selectbarang'),
    url(r'^Selectallbarang/$', SelectAll.as_view(), name='Selectallbarang'),
    url(r'^User/List/$', ReadUser.as_view(), name='Read-User'),
    url(r'^alldistributor/$', SelectAllDistributor.as_view(), name='alldist'),
    url(r'^loginrequest/$', loginview.as_view(), name='loginrequest'),
    url(r'^User/Add/$', RegisterUser.as_view(), name='Add-User'),
    url(r'^User/Update/(?P<username>[\w.+_-]+)/$', UpdateUser.as_view(), name='Edit-User'),
]
