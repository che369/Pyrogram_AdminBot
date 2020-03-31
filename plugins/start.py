#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Anand PS Kerala

# the logging things
import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

import os
import sqlite3

from config import Config
from translation import Translation
import pyrogram
from pyrogram import Client, Filters, ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton
from database import TRChatBase
from sql.sql import *

STARTKEY = [[InlineKeyboardButton("📚 Commands", callback_data="commands"), InlineKeyboardButton("ℹ️ Info", url="https://t.me/keralasbots")]]
STARTKEY += [[InlineKeyboardButton("★ Jinja", callback_data="jinja")]]
BACKKEY = [[InlineKeyboardButton("🔙 Back", callback_data="start_back")]]

@pyrogram.Client.on_message(pyrogram.Filters.command(["start"]))
async def start(bot, update):
    await bot.send_message(chat_id=update.chat.id, text=Translation.START, parse_mode="html", disable_web_page_preview=True, reply_to_message_id=update.message_id, reply_markup=InlineKeyboardMarkup(STARTKEY))

@pyrogram.Client.on_callback_query(pyrogram.Filters.callback_data("start_back"))
async def start_back(bot, update):
    await bot.edit_message_text(chat_id=update.message.chat.id, text=Translation.START, parse_mode="html", disable_web_page_preview=True, message_id=update.message.message_id, reply_markup=InlineKeyboardMarkup(STARTKEY))


@pyrogram.Client.on_callback_query(pyrogram.Filters.callback_data("commands"))
async def commands(bot, update):
    await bot.edit_message_text(chat_id=update.message.chat.id, text=Translation.COMMAND, parse_mode="html", disable_web_page_preview=True, message_id=update.message.message_id, reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("👤Private Commands", url="https://t.me/keralasbots"), InlineKeyboardButton("👷 Admin Commands", url="https://docs.pyrogram.org"),], [InlineKeyboardButton("🔙 Back", callback_data="start_back")]]))

@Client.on_callback_query(Filters.callback_data("jinja"))
async def jinja(bot, update):
    jin = [[InlineKeyboardButton("★ Set Jinja", callback_data="setjinja")]]
    jin += BACKKEY
    jinjamark = InlineKeyboardMarkup(jin)
    view = vjinja(update.from_user.id)
    if view == None:
        jinja = "None"
    else:
        jinja = str(view)
    await bot.edit_message_text(chat_id=update.message.chat.id, text=jinja, message_id=update.message.message_id, reply_markup=jinjamark)

@Client.on_callback_query(Filters.callback_data("setjinja"))
async def setjinja(bot, update):
    back = InlineKeyboardButton(BACKKEY)
    await bot.edit_message_text(chat_id=update.message.chat.id, text="Now send me the jinja", message_id=update.message.message_id, reply_markup=back)
    s = input("Enter jinja:")
    jinja(update.from_user.id, update.message. reply_to_message.text)
    await bot.edit_message_text(chat_id=update.message.chat.id, text="Successfully set jinja", message_id=update.message.message_id, reply_markup=back)

    
