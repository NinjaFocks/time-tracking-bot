import datetime

def get_date():
	return datetime.datetime.now().strftime('%d-%m-%Y')

def get_date_time():
	return datetime.datetime.now().strftime('%d-%m-%Y %H:%M')
	
def create_file():
	date = get_date()
	with open(date + '.csv', 'wb') as csvFile:
		filewriter = csv.writer(csvFile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
		filewriter.writerow(['TaskName', 'StartedTime', 'FinishedTime','InProgress'])
		
def start_task(task_name):
	date = get_date()