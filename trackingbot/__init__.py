from phial import Phial
from config import SLACK_API_TOKEN

bot = Phial(SLACK_API_TOKEN)

#from teabot import tea, fun  # noqa: F401, E402
from trackingbot import commands