import csv
from trackingbot.dates import get_date, get_time
from pathlib import Path
import shutil
from config import CSV_FILE_LOCATION
from datetime import datetime
	
def create_file():
	date = get_date()
	print('creating file')
	with open(CSV_FILE_LOCATION + date + '.csv', 'w', newline='') as csvFile:		
		filewriter = csv.writer(csvFile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)		
		filewriter.writerow(['TaskName', 'StartedTime', 'FinishedTime','Progress'])
		csvFile.close()
	
		
def start_task(task_name):
	date = get_date()
	time = get_time()	
	
	today_file = Path(CSV_FILE_LOCATION + date + '.csv')
	if (not today_file.is_file()):
		create_file()	
	else:
		finish_task()
		
	with open(CSV_FILE_LOCATION + date + '.csv', 'a', newline='') as csvFile:
		print('start_task opened file')
		filewriter = csv.writer(csvFile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)		
		filewriter.writerow([task_name, time, '', 'InProgress'])		
	print('start_task closed file')
		
def finish_task():
	date = get_date()
	time = get_time()
	
	csvLocation = CSV_FILE_LOCATION + date + '.csv'
	tempLocation = CSV_FILE_LOCATION + date + '_temp.csv'
	
	with open(csvLocation, 'r', newline='') as csvFile, open(tempLocation, 'w', newline='') as tempfile:	
		filereader = csv.reader(csvFile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
		filewriter = csv.writer(tempfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
		print('finish_task opened file')
	
		for row in filereader:
			if (row[3] == 'InProgress'):
				row[2] = time
				row[3] = 'Finished'
				filewriter.writerow(row)			
			else: 
				filewriter.writerow(row)
	
	print('finish_task closed file')
	shutil.move(tempfile.name, csvFile.name)
	
def get_summary():
	date = get_date()
	csvLocation = CSV_FILE_LOCATION + date + '.csv'
	
	summary = ''
	
	with open(csvLocation, 'r', newline='') as csvFile:
		print('summary opened file')
		filereader = csv.reader(csvFile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)	
		for row in filereader:
			if (row[0] == 'TaskName'):
				summary = str(row[0]) + ' - ' + 'Time Taken\n'				
			elif (row[3] == 'InProgress'):
				summary = summary + row[0] + ' - ' + 'In Progress' + '\n'			 
			else:
				time = datetime.strptime(row[2], '%H:%M') - datetime.strptime(row[1], '%H:%M')
				summary = summary + row[0] + ' - ' + str(time) + '\n'
	print('summary closed file')	
	return summary
			
		
