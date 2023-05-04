from email import message

import telebot
import types
from telebot import types
import config

bot = telebot.TeleBot('6190291865:AAHW2e66_Z38xAQb3S5MSvRfNb28WitHjY0')


@bot.message_handler(commands=['/start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Поздороваться")
    btn2 = types.KeyboardButton("Задать вопрос")
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id, text="Я могу тебе помочь с некоторыми вопросами".format(message.from_user), reply_markup=markup)

@bot.message_handler(content_types=['text'])
def func(message):
    if(message.text == "Поздороваться"):
        bot.send_message(message.chat.id, text="Привет!")
    elif(message.text == "Задать вопрос"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("За что вуз начисляет абитуриентам дополнительные баллы?")
        btn2 = types.KeyboardButton("Есть ли льготы для участников олимпиад и других соревнований?")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn1, btn2, back)
        bot.send_message(message.chat.id, text="Задай мне вопрос", reply_markup=markup)

    elif (message.text == "За что вуз начисляет абитуриентам дополнительные баллы?"):
        bot.send_message(message.chat.id, "Дополнительные баллы при поступлении в вуз могут начислить по результатам портфолио. Затем дополнительные баллы суммируют с баллами за ЕГЭ, что позволяет абитуриенту занять лучшее положение в конкурсном списке.")

    elif message.text == "Есть ли льготы для участников олимпиад и других соревнований?":
        bot.send_message(message.chat.id, text="Льготы при поступлении в вуз получают победители и призеры школьных олимпиад из Перечня, который составило Минобрнауки.")

    elif (message.text == "Вернуться в главное меню"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("Поздороваться")
        button2 = types.KeyboardButton("Задать вопрос")
        markup.add(button1, button2)
        bot.send_message(message.chat.id, text="Вы вернулись в главное меню", reply_markup=markup)
    else:
        bot.send_message(message.chat.id, text="На такую комманду я не запрограммирован")

bot.polling(none_stop=True)