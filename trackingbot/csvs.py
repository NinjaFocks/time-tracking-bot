import csv
from trackingbot.dates import get_date, get_time
from pathlib import Path
import sys
	
def create_file():
	date = get_date()
	print('creating file')
	with open('C:/Git/time-tracking-bot/trackingbot/csvFiles/' + date + '.csv', 'w', newline='') as csvFile:		
		filewriter = csv.writer(csvFile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)		
		filewriter.writerow(['TaskName', 'StartedTime', 'FinishedTime','Progress'])
		csvFile.close()
	
		
def start_task(task_name):
	date = get_date()
	time = get_time()	
	
	today_file = Path('C:/Git/time-tracking-bot/trackingbot/csvFiles/' + date + '.csv')
	if (not today_file.is_file()):
		create_file()	
	print('opening file')
	csvFile = open('C:/Git/time-tracking-bot/trackingbot/csvFiles/' + date + '.csv', 'a', newline='')	
	print('opened file')
	filewriter = csv.writer(csvFile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)		
	filewriter.writerow([task_name, time, '', 'InProgress'])
	csvFile.close()
	print('closed file')
		
 #def finish_task(task_name):
	#date = get_date()
	#time = get_time()
	#file = csv.reader(open('C:/Git/time-tracking-bot/trackingbot/csvFiles/' + date + '.csv', 'r'), delimiter=',')
	#for row in file:
		#if (task_name == row[0]):
			