#version: 1.0

from telegram.ext import Updater, CommandHandler
from telegram import update, ChatAction
from Functions.BasicFunctions import functions
import random

token = functions.config()
updater = Updater(token=token, use_context=True)

#Commands
def start(update, context):
    """ Saluda a hikari """
    context.bot.send_chat_action(chat_id=update.effective_chat.id, action=ChatAction.TYPING)
    saludos = ("Hola Humano :)", "Holaa", "Aqui estoy 👋", "Hikari: On \n:b")
    context.bot.send_message(chat_id=update.effective_chat.id, text=random.choice(saludos))

def help(update, context):
    """Acerca de Hikari Bot"""
    file = open ('Resources/help.txt','r')
    help = file.read()
    file.close()
    context.bot.send_chat_action(chat_id=update.effective_chat.id, action=ChatAction.TYPING)
    context.bot.send_message(chat_id=update.effective_chat.id, text=help)

def rules(update, context):
    """Reglas de la comunidad AprenderPython"""
    file = open ('Resources/rules.txt','r')
    rules = file.read()
    file.close()
    context.bot.send_chat_action(chat_id=update.effective_chat.id, action=ChatAction.TYPING)
    context.bot.send_message(chat_id=update.effective_chat.id, text=rules)


#Listeners 
start_handler = CommandHandler("start", start)
help_handler = CommandHandler("help", help)
rules_handler = CommandHandler("rules", rules)

updater.dispatcher.add_handler(start_handler)
updater.dispatcher.add_handler(help_handler)
updater.dispatcher.add_handler(rules_handler)

updater.start_polling()