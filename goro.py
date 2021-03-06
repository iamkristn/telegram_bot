import random
import telebot
bot = telebot.TeleBot('2026390830:AAE4pD3mspdqpi3eCpsMigaIrozshbUSwKg')
from telebot import types
first = ["Начало дня может оказаться сложным, особенно с точки зрения общения.","Оптимальный день для того, чтобы решиться поработать сверхурочно!","Будьте осторожны, сегодня звёзды могут повлиять на ваше финансовое состояние.","Лучшее время для того, чтобы начать новые трудовые отношения или разобраться со старыми.","Плодотворный день для того, чтобы разобраться с накопившимися делами."]
second = ["Те, кто сегодня нацелен выполнить множество дел, должны помнить про", "Но помните, что даже в этом случае не стоит забывать про","Если поедете за город, заранее подумайте про","Если у вас упадок сил, обратите внимание на","Помните, что мысли материальны, а значит вам в течение дня нужно постоянно думать про"]
second_add = ["работу и деловые вопросы, которые могут так некстати помешать планам.", "отношения с друзьями и коллегами.","себя и своё здоровье, иначе к вечеру возможен полный упадок сил.","бытовые вопросы — особенно те, которые вы не доделали вчера.","отдых, чтобы не превратить себя в загнанную лошадь в конце месяца."]
third = ["Случайное недопонимание может повлечь за собой тайные обиды, если вовремя не прояснить все.","Да, можно столкнуться с трудностями, но желание бросить начатое не появится даже у тех, кто обычно отступает перед любой преградой.","Даже если вы не сможете уменьшить влияние ретроградного Меркурия, то хотя бы доведите дела до конца.","Не нужно бояться случайных встреч — сегодня то самое время, когда они значат многое.","Если встретите незнакомца на пути — проявите участие, и тогда эта встреча посулит вам приятные хлопоты."]
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "/start":
        bot.send_message(message.from_user.id, "Привет! Я расскажу тебе самый точный гороскоп на сегодня.")
        keyboard = types.InlineKeyboardMarkup()
        l = ['Овен', 'Телец', 'Близнецы', 'Рак', 'Лев', 'Дева', 'Весы', 'Скорпион', 'Стрелец', 'Козерог', 'Водолей', 'Рыбы' ]
        button_list = [types.InlineKeyboardButton(text=x, callback_data='zodiac') for x in l]
        keyboard.add(*button_list)
        bot.send_message(message.from_user.id, text='Выбери свой знак зодиака', reply_markup=keyboard)
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Напиши /start")
    else:
        bot.send_message(message.from_user.id, "Это очень сложно, боюсь, что я не понимаю тебя. Напиши /start.")
@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == "zodiac": 
        msg = random.choice(first) + ' ' + random.choice(second) + ' ' + random.choice(second_add) + ' ' + random.choice(third)
        bot.send_message(call.message.chat.id, msg)
bot.polling(none_stop=True, interval=0)
