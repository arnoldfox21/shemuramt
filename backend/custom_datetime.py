import datetime

def getdate():

	date = datetime.datetime.now().strftime("%d")

	return date

def getmonth():

	month = datetime.datetime.now().strftime("%m")

	return month

def gethour():

	hour = datetime.datetime.now().strftime("%H")

def getyear():

	year = datetime.datetime.now().strftime("%Y")

	return year