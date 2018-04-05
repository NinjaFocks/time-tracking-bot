from phial import command, Response
from datetime import datetime, timedelta
from threading import Thread, Lock
from time import sleep
from fractions import Fraction
from trackingbot import bot
from config import TEST_TRACKING_CHANNEL_ID
#from trackingbot.dates import get_date, get_date_time

#making changes to add develop branch

@bot.command("echo <text>")
def echo(text):
	bot.send_message(Response(TEST_TRACKING_CHANNEL_ID, text=text))
	

@bot.command("start <task_name>")
def start(task_name):
	bot.send_message(Response(TEST_TRACKING_CHANNEL_ID, text=task_name + " started"))
	
@bot.command("finish")
def finish():
	bot.send_message(Response(TEST_TRACKING_CHANNEL_ID, text="Task finished"))
	
@bot.command("date")
def date():
	date = get_date()
	bot.send_message(Response(TEST_TRACKING_CHANNEL_ID, text=date))
	
@bot.command("datetime")
def datetime():
	datetime = get_date_time()
	bot.send_message(Response(TEST_TRACKING_CHANNEL_ID, text=datetime))
