from phial import command, Response
from datetime import datetime, timedelta
from threading import Thread, Lock
from time import sleep
from fractions import Fraction
from trackingbot import bot
from config import TEST_TRACKING_CHANNEL_ID

#making changes to add develop branch

@bot.command("echo")
def echo():
	bot.send_message(Response(TEST_TRACKING_CHANNEL_ID, text="Hello World."))