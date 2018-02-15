from slackbot.bot import respond_to
from slackbot.bot import listen_to
import re


@respond_to('hi', re.IGNORECASE)
def hi(message):
    message.reply("G'day mate!!")
    # react with thumb up emoji
    message.react('+1')

@respond_to('bye', re.IGNORECASE)
def bye(message):
    message.reply("See ya mate!!")
    message.react('+1')
