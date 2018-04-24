from phial import command, Response
from datetime import datetime, timedelta
from threading import Thread, Lock
from time import sleep
from fractions import Fraction
from trackingbot import bot
from config import TEST_TRACKING_CHANNEL_ID
from trackingbot.dates import get_date, get_date_time
from trackingbot.csvs import start_task, finish_task, get_summary

#making changes to add develop branch

@bot.command("echo <text>")
def echo(text):
	return text


@bot.command("start <task_name>")
def start(task_name):
	start_task(task_name)
	return task_name + ' started'
	
@bot.command("finish")
def finish():
	finish_task()
	return 'Task finished'
	
@bot.command("date")
def date():
	date = get_date()
	return date
	
@bot.command("datetime")
def datetime():
	datetime = get_date_time()
	return datetime

@bot.command("summary")
def summary():
	return get_summary()

@bot.command("help")
def help():
	commands = ''
	commands += '!start <task_name> - Start a new task\n !finish - Finish current and previous tasks\n !date - Get the current date in DD-MM-YYYY format\n !datetime - Get the current date and time in DD-MM-YYYY HH:MM format\n !summary - Get a summary of today\'s tasks, returns a list of task names and time spent'
	return commands