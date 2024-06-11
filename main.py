import telebot
from telebot import types

TOKEN = "7185370622:AAHh_dec6TYFPuN2dLWbZX7tsaH8oBopi78"
bot = telebot.TeleBot(TOKEN)

def main():
    bot.polling(none_stop=True, interval=0) #Опрос ботом сервера телеграма для того, чтобы регистирировать последние сообения пользователей.

@bot.message_handler(content_types=['text']) #Данная строчка говорит о том, что следующая после неё функция занимается обработкой текстовых сообщений
def get_text_messages1(message):#Фунция для обработки текстовых сообщений
    if message.text.lower() == "/start" or message.text.lower() ==  "привет":
        bot.send_message(message.from_user.id, "Привет, я бот, дающий определения. Я знаю некоторые экономические термины из таких разделов как: микроэкономика, макроэкономика и мировая экономика, выбери какой-то из них!")
    elif message.text.lower() == "микроэкономика":
        keyboard = types.InlineKeyboardMarkup()
        key_dom = types.InlineKeyboardButton(text='Домохозяйство', callback_data='dom')
        keyboard.add(key_dom)
        key_rin = types.InlineKeyboardButton(text='Рынок', callback_data='rin')
        keyboard.add(key_rin)
        key_spros = types.InlineKeyboardButton(text='Спрос', callback_data='spros')
        keyboard.add(key_spros)
        key_pred = types.InlineKeyboardButton(text='Предложение', callback_data='pred')
        keyboard.add(key_pred)
        key_nakop = types.InlineKeyboardButton(text='Накопление', callback_data='nakop')
        keyboard.add(key_nakop)
        question = 'Микроэкономика'
        bot.send_message(message.from_user.id, text=question, reply_markup=keyboard)
    elif message.text.lower() == "макроэкономика":
        keyboard1 = types.InlineKeyboardMarkup()
        key_inf = types.InlineKeyboardButton(text='Инфляция', callback_data='inf')
        keyboard1.add(key_inf)
        key_def = types.InlineKeyboardButton(text='Дефляция', callback_data='def')
        keyboard1.add(key_def)
        key_mon = types.InlineKeyboardButton(text='Монополия', callback_data='mon')
        keyboard1.add(key_mon)
        key_vvp= types.InlineKeyboardButton(text='ВВП', callback_data='vvp')
        keyboard1.add(key_vvp)
        key_nazd= types.InlineKeyboardButton(text='Национальный доход', callback_data='nazd')
        keyboard1.add(key_nazd)
        question = 'Макроэкономика'
        bot.send_message(message.from_user.id, text=question, reply_markup=keyboard1)
    elif message.text.lower() == "мировая экономика":
        keyboard2 = types.InlineKeyboardMarkup()
        key_mirecint = types.InlineKeyboardButton(text='Мировые экономические интеграции', callback_data='mirecint')
        keyboard2.add(key_mirecint)
        key_mtorg = types.InlineKeyboardButton(text='Международная торговля', callback_data='mtorg')
        keyboard2.add(key_mtorg)
        key_imp = types.InlineKeyboardButton(text='Импорт', callback_data='imp')
        keyboard2.add(key_imp)
        key_exp= types.InlineKeyboardButton(text='Экспорт', callback_data='exp')
        keyboard2.add(key_exp)
        question = 'Мировая экономика'
        bot.send_message(message.from_user.id, text=question, reply_markup=keyboard2)
    elif message.text.lower() == "/help":
        bot.send_message(message.from_user.id, "Пользоваться мною очень просто! Выбери раздел, который тебя интересует, и сможешь получить термины: микроэкономика, макроэкономика, мировая экономика")
    else:
        bot.send_message(message.from_user.id,"Такго раздела пока что нет!")
@bot.callback_query_handler(func=lambda call: True)#Данная строка оповещает о том, что следующая функция будет обрабатывать данные из телеграм-клавиатуры для выбора вариантов
def callback_worker(call):#Функция обработки клавиатуры
    if call.data == "dom": #call.data это callback_data, которую мы указали при объявлении кнопки
        bot.send_message(call.message.chat.id, "это законодательно закреплённая форма хозяйственной деятельности, объединяющая людей отношениями, возникающими при организации их совместного быта.")
        bot.send_photo(call.message.chat.id, open('dom.jpg', 'rb'))
    elif call.data == "rin":
        bot.send_message(call.message.chat.id,"это совокупность институтов, обеспечивающих взаимодействие между покупателями и продавцами и способствующих обмену.")
        bot.send_photo(call.message.chat.id, open('rin.jpg', 'rb'))
    elif call.data == "spros":
        bot.send_message(call.message.chat.id," это зависимость между ценой и количеством товара, которое потребители могут и хотят купить по строго определённой стоимости в конкретный промежуток времени.")
        bot.send_photo(call.message.chat.id, open('spros.jpg', 'rb'))
    elif call.data == "pred":
        bot.send_message(call.message.chat.id," это количество какого-либо блага (товара или услуги), представленное для продажи на рынке.")
        bot.send_photo(call.message.chat.id, open('pred.jpg', 'rb'))
    elif call.data == "nakop":
        bot.send_message(call.message.chat.id,"превращение части прибыли в капитал, увеличение запасов материалов, имущества, денежных средств, наращивание капитала, основных средств государством, предприятиями, предпринимателями, домашними хозяйствами.")
        bot.send_photo(call.message.chat.id, open('nakop.jpg', 'rb'))

    elif call.data == "inf":
        bot.send_message(call.message.chat.id,"это устойчивый процесс снижения покупательной способности денег, их обесценивание.")
        bot.send_photo(call.message.chat.id, open('inf.jpeg', 'rb'))
    elif call.data == "def":
        bot.send_message(call.message.chat.id,"снижение общего уровня цен на товары и услуги. Это процесс, противоположный инфляции.")
        bot.send_photo(call.message.chat.id, open('def.jpeg', 'rb'))
    elif call.data == "vvp":
        bot.send_message(call.message.chat.id,"это макроэкономический показатель, который отражает рыночную стоимость всех конечных товаров и услуг, произведённых за год во всех отраслях экономики на территории конкретного государства для потребления, экспорта и накопления.")
        bot.send_photo(call.message.chat.id, open('vvp.jpeg', 'rb'))
    elif call.data == "nazd":
        bot.send_message(call.message.chat.id,"валовый доход, созданный (заработанный) в результате использования принадлежащих государству ресурсов как внутри страны, так и за границей.")
        bot.send_photo(call.message.chat.id, open('nazd.jpg', 'rb'))
    elif call.data == "mon":
        bot.send_message(call.message.chat.id,"это модель рынка, на котором в производстве или распределении того или иного продукта доминирует одно предприятие, устанавливая полный контроль над ценами.")
        bot.send_photo(call.message.chat.id, open('mon.jpg', 'rb'))


    elif call.data == "mirecint":
        bot.send_message(call.message.chat.id,"процесс объединения различных стран или регионов для совместной работы в экономической сфере. ")
        bot.send_photo(call.message.chat.id, open('mirecint.jpg', 'rb'))
    elif call.data == "mtorg":
        bot.send_message(call.message.chat.id,"обмен товарами и услугами между различными странами. Она осуществляется через импорт (покупка товаров из других стран) и экспорт (продажа товаров за рубеж). ")
        bot.send_photo(call.message.chat.id, open('mtorg.jpg', 'rb'))
    elif call.data == "imp":
        bot.send_message(call.message.chat.id,"процесс приобретения товаров и услуг из других стран для использования на внутреннем рынке. Страна, принимающая импортированные товары, обычно платит за них валютой или другими товарами.")
        bot.send_photo(call.message.chat.id, open('imp.jpg', 'rb'))
    elif call.data == "exp":
        bot.send_message(call.message.chat.id,"процесс продажи товаров и услуг за пределами страны. Экспорт позволяет странам получать доход от продажи своей продукции на мировом рынке, способствует развитию экономики и созданию рабочих мест.")
        bot.send_photo(call.message.chat.id, open('exp.jpg', 'rb'))

main()#Вызов главной функции, обеспечивающей непрерывную работу бота