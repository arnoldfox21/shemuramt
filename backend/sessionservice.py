
from backend.models import Distributor, User, Settings, Session_user

def getUserLogined(id):
	return User.objects.get(pk = id)

def getDistributorLogined(id):
	return Distributor.objects.get(pk = id)

def webconfig(config):
	
	Con = Settings.objects.filter(pk = config)
	con = Con.first()
	return con

def getlock(status):
	co = Session_user.objects.filter(user_id=status)
	config = co.first()
	return config