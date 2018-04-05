import datetime

def get_date():
	return datetime.datetime.now().strftime('%d-%m-%Y')

def get_date_time():
	return datetime.datetime.now().strftime('%d-%m-%Y %H:%M')

def get_time():
	return datetime.datetime.now().strftime('%H:%M')