
from django import forms
from django.forms import ModelForm
from backend.models import Contact, Distributor, User, Barang, Contact_reply


class ContactForm(ModelForm):
	class Meta:
		model = Contact
		fields = ['nama', 'umail','subject', 'pesan']
		labels = {
			"umail": "Email"
					}
		widgets = {
			'pesan': forms.Textarea(attrs={'class': 'materialize-textarea'}),
		}

class distributor(ModelForm):

	class Meta:
		model = Distributor
		fields = ['nama', 'pswd', 'umail', 'tgl_lahir','alamat', 'telp','foto', 'jenis_kelamin', 'joined_time']
		labels = {
			"umail": "Email",
			'pswd': 'Password',
			'tgl_lahir': 'Lahir',
			'joined_time': 'Waktu bergabung'
					}
		widgets = {
			'jenis_kelamin': forms.TextInput(attrs={'readonly':'readonly'}),
			'joined_time': forms.TextInput(attrs={'readonly':'readonly'}),
			'alamat': forms.TextInput(attrs={'readonly':'readonly'}),
			'foto': forms.TextInput(attrs={'type':'hidden'})
		}

class Petugas(ModelForm):
	class Meta:
		model = User
		fields = ['id','username', 'pswd', 'umail', 'jabatan']
		labels = {
			"umail": "Email",
			'pswd': 'Password'
					}
		widget = {
			'id': forms.HiddenInput()
		}
		
class Contact_r(ModelForm):

	class Meta:
		model = Contact_reply
		fields = ['pesan']
		labels = {
			"pesan": "Tulis pesan"
					}
		widgets = {
			'pesan': forms.Textarea(attrs={'class': 'materialize-textarea'}),
		}

class Form_barang(ModelForm):

	class Meta:
		model = Barang
		fields = ['id', 'nm_barang', 'harga_satuan', 'stock', 'berat', 'warna', 'ket_tambahan']
		labels = {
			"nm_barang": "Nama barang"
					}