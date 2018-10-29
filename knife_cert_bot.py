#!/usr/bin/python
# -*- coding: utf-8 -*-
import telebot
from telebot import types
import const


# Подключаем через TelegramAPI бота с которым будем работать
bot = telebot.TeleBot(const.API_TOKEN)

# Создаем меню бота
main_menu = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)


# Создаем кнопки в меню выбора производителя ножей, подтягивая переменные из файла const.py
# main_menu.add(*[types.InlineKeyboardButton(knife_vendor) for knife_vendor in const.knife_vendors])

#def start(m):
#    main_menu.add(*[types.InlineKeyboardButton(knife_vendor) for knife_vendor in const.knife_vendors])
#    msg = bot.send_message(m.chat.id, 'Выберите производителя ножа', reply_markup=main_menu)
#    bot.register_next_step_handler(msg, const.knife_vendors)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Добро пожаловать! \nСпециально для Вас здесь собраны сертификаты для ножей из магазина brutallica.ru\n",
                 reply_markup=main_menu)


bot.polling()

# keyboard.add(*[types.KeyboardButton(name) for name in ['Шерлок Холмс', 'Доктор Ватсон']])
#    bot.send_message(m.chat.id, 'Кого выбираешь?',
#                     reply_markup=keyboard)

# btn_coldsteel = types.KeyboardButton('Cold Steel')
# btn_ontario = types.KeyboardButton('Ontario')
# btn_spyderco = types.KeyboardButton('Spyderco')
# btn_kershaw = types.KeyboardButton('Kershaw')
# btn_realsteel = types.KeyboardButton('RealSteel')
# btn_crkt = types.KeyboardButton('CRKT')
# btn_mora = types.KeyboardButton('MORA')
# btn_esee = types.KeyboardButton('ESEE')
# btn_buck = types.KeyboardButton('BUCK')
# btn_ganzo = types.KeyboardButton('GANZO')
# btn_mrblade = types.KeyboardButton('Mr.BLADE')
# btn_kizlyar = types.KeyboardButton('Kizlyar Supreme')
# btn_steelwill = types.KeyboardButton('Steel Will')
# btn_benchmade = types.KeyboardButton('Benchmade')
# btn_marser = types.KeyboardButton('Marser')
# btn_bestech = types.KeyboardButton('Bestech')
# btn_ruike = types.KeyboardButton('Ruike')
# btn_reptilian = types.KeyboardButton('Reptilian')


# Отображаем кнопки на клавитуре
# main_menu.add(btn_coldsteel, btn_ontario, btn_spyderco, btn_kershaw, btn_realsteel, btn_crkt, btn_mora, btn_esee,
#                btn_buck, btn_ganzo, btn_mrblade, btn_kizlyar, btn_steelwill, btn_benchmade, btn_marser, btn_bestech,
#                btn_ruike, btn_reptilian)


# Приветственное сообщение от бота
# @bot.message_handler(commands=['start'])
# def send_welcome(message):
#    bot.reply_to(message, "Добро пожаловать! \nСпециально для Вас здесь собраны сертификаты для ножей!\n",
#                 reply_markup=main_menu)


# @bot.message_handler(func=lambda message: True)
# def echo_all(message):
#    bot.reply_to(message, message.text, reply_markup=main_menu)
