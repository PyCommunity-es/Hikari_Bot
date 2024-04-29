import asyncio
from functools import wraps
from telegram import Update
from telegram.ext import ContextTypes
from telegram.constants import ChatAction


def action_typing(func):
    @wraps(func)
    async def wrapper(update: Update, context: ContextTypes.DEFAULT_TYPE, *args, **kwargs):
        await context.bot.send_chat_action(chat_id=update.effective_chat.id, action=ChatAction.TYPING)
        return await func(update, context, *args, **kwargs)
    return wrapper
        