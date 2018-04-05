from trackingbot.dates import get_date, get_time
	
def create_file():
	date = get_date()
	with open(date + '.csv', 'wb') as csvFile:
		filewriter = csv.writer(csvFile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
		filewriter.writerow(['TaskName', 'StartedTime', 'FinishedTime','Progress'])
		
def start_task(task_name):
	date = get_date()
	time = get_time()
	with open(date + '.csv') as csvFile:
		filewriter = csv.writer(csvFile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
		filewriter.writerow([task_name, time, '', 'InProgress'])
		
def finish_task(task_name)
	date = get_date()
	time = get_time()
	file = csv.reader(open(date + '.csv', 'rb'), delimiter-',')
	for row in file:
		if 
		