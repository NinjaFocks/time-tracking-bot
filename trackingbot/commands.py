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
