from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder
from aiogram import types
from aiogram.types import InlineKeyboardButton
from urllib.parse import quote



def get_share_keyboard(repost, bot_link):
    print(quote(repost))
    vk_link = f'https://vk.com/share.php?url={quote(bot_link)}&title={quote(repost)}'
    wa_link = f'https://api.whatsapp.com/send?text={quote(repost)}\n{bot_link}/'
    keyboard = InlineKeyboardBuilder()
    keyboard.row(InlineKeyboardButton(text='Поделиться в VK', url=vk_link))
    keyboard.row(InlineKeyboardButton(text="Поделиться в WhatsApp", url=wa_link))

    return keyboard

def get_finish_keyboard():
    keyboard = ReplyKeyboardBuilder()

    keyboard.row(types.KeyboardButton(text='Связаться с сотрудником'))
    keyboard.row(types.KeyboardButton(text='Попробовать ещё раз'))
    keyboard.row(types.KeyboardButton(text='Поделиться результатом'))

    return keyboard