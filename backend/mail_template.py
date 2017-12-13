
def template_mail( nm_supl, jmlh, nama_bahan):
	text = '<!DOCTYPE html><html lang="en"><head></head><body>Yth. Saudara %s,<br/> kita membutuhkan %s %s mohon segera dikirimkan ke UD kami, jika tidak bisa memenuhi permintaan kami mohon hubungi kami.<br/><br/> terima kasih,<br/><br/> hormat kami<br/><b>UD Shemura Mikasa Tani.</b></body></html>' %(nm_supl, jmlh, nama_bahan)
	return text