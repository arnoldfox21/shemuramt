from itertools import *
from django.db import connection
from django.db.models import Avg, Sum, Q
from backend.models import Settings, Barang, Transaksi
import re
from django.db.models import Q

def getcolor(id):
	
	return Settings.objects.get(pk = id)

def normalize_query(query_string,
	findterms=re.compile(r'"([^"]+)"|(\S+)').findall,
	normspace=re.compile(r'\s{2,}').sub):
	return [normspace(' ',(t[0] or t[1]).strip()) for t in findterms(query_string)]

def get_query(query_string, search_fields):

	query = None 
	terms = normalize_query(query_string)
	for term in terms:
		or_query = None
		for field_name in search_fields:
			q = Q(**{"%s__icontains" % field_name: term})
			if or_query is None:
				or_query = q
			else:
				or_query = or_query | q
		if query is None:
			query = or_query
		else:
			query = query & or_query
	return query

def db_barang(row):
	get_barang = Barang.objects.all()[:row]
	return get_barang


def Helper_ObjectRaw(var):
	with connection.cursor() as cursor:
		cursor.execute(var)
		col_names = [desc[0] for desc in cursor.description]
		row = cursor.fetchall()
		
	return row


# def icontain(alpha, beta, delta):
# 	val = "%s__icontains" % (beta)
# 	p = alpha.objects.filter(val = delta)
# 	return p