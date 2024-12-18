import os
import json
from gc import callbacks
from gettext import install
from traceback import print_tb

import settings








import telebot
from pyexpat.errors import messages
from telebot import types





def g(xop):
    unique_names = []
    for name in xop:
        if name not in unique_names:
            unique_names.append(name)
    return unique_names





admins=[settings.ADMINER]
users=[]
visitors=[]
names=[]
contracts1=[]
contracts2=[]
contracts3=[]
contracts4=[]







bot=telebot.TeleBot(settings.API_KEY)


@bot.message_handler(commands=['start'])
def main(message):
    markup=types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Админ',callback_data='admin'))
    markup.add(types.InlineKeyboardButton('Сотрудник',callback_data='user'))
    bot.send_message(message.chat.id,'Добро пожаловать в бот DocPower!',reply_markup=markup)
    print(message)




@bot.callback_query_handler(func=lambda callback: True)
def callback_message(callback_query):
    if callback_query.data == 'admin':
        # bot.send_message(callback_query.message.chat.id,'hjvjgv')
        if admins.count(callback_query.from_user.id)  :
            markup=types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton('Предоставить доступ к контрактам',callback_data='doc'))
            markup.add(types.InlineKeyboardButton('Удалить сотрудника',callback_data='deleter'))
            bot.send_message(callback_query.message.chat.id,'Выберите опцию',reply_markup=markup)
            print(callback_query.message.chat.id)
            bot.answer_callback_query(callback_query.id)







        else:
            bot.send_message(callback_query.message.chat.id,'Вы не обладаете правами администратора')
            print(callback_query)
            bot.answer_callback_query(callback_query.id)

    elif callback_query.data =='user':
        if users.count(callback_query.from_user.id):
            markup=types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton('Посмотрите документацию',callback_data='viewdoc'))
            bot.send_message(callback_query.message.chat.id,'Получить доступ',reply_markup=markup)
            bot.answer_callback_query(callback_query.id)
        elif admins.count(callback_query.from_user.id):
            bot.send_message(callback_query.message.chat.id, 'Вы не являетесь сотрудником')
            bot.answer_callback_query(callback_query.id)







        else:
            markup=types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton('Зарегистрироваться', callback_data='registr'))
            bot.send_message(callback_query.message.chat.id,'Передайте свои данные администратору',reply_markup=markup)
            bot.answer_callback_query(callback_query.id)
    elif callback_query.data=='registr':
        for callback_query.message.from_user.id in admins:
            markup=types.InlineKeyboardMarkup()
            btn1 = types.InlineKeyboardButton('Предоставить права администратора',callback_data='adminrights')
            markup.row(btn1)
            btn2=types.InlineKeyboardButton('Предоставить права сотрудника',callback_data='userrights')
            btn3=types.InlineKeyboardButton('Отклонить в предоставлении прав',callback_data='decline')
            markup.row(btn2, btn3)
            # names.append(callback_query.message.chat.first_name)
            # print(len(list(set(names))))
            # qup=len(list(set(names)))
            # qupi=list(set(names))
            # print(qup)
            # print(qupi)
            bot.send_message(callback_query.message.from_user.id,f'{callback_query.message.chat.first_name} хочет зарегистрироваться в качестве сотрудника',reply_markup=markup)
            bot.answer_callback_query(callback_query.id)
            visitors.append(callback_query.message.chat.id)
        bot.send_message(callback_query.message.chat.id,'Ждите рассмотрения вашей заявки администратором')
    elif callback_query.data=='adminrights':
        for callback_query.message.chat.id in list(set(visitors)):
            admins.append(callback_query.message.chat.id)
            print(admins)
            bot.send_message(callback_query.message.chat.id,'Вам были предоставлены права администратора')
        bot.answer_callback_query(callback_query.id)
    elif callback_query.data=='userrights':
        for callback_query.message.from_user.id in list(set(visitors)):
            ret=bot.get_chat(callback_query.message.from_user.id)
            print(ret.first_name)
            users.append(callback_query.message.from_user.id)
            print('users=', callback_query)
            bot.send_message(callback_query.message.from_user.id,'Вам были предоставлены права сотрудника')
            names.append(ret.first_name  )
            print(names)
            print('Имя сотрудника', callback_query.message.from_user.first_name)
            print(len(list(set(names))))
            qup = len(list(set(names)))
            qupi = list(set(names))
            print(qup)
            print(qupi)
        bot.answer_callback_query(callback_query.id)
        visitors.clear()
    if callback_query.data=='decline':
        for callback_query.from_user.id in list(set(visitors)):
            bot.send_message(callback_query.from_user.id,'Получение прав было отклонено администратором')
        bot.answer_callback_query(callback_query.id)






    if callback_query.data=='doc':
        markup=types.InlineKeyboardMarkup()
        bt1=types.InlineKeyboardButton('Контракт №1',callback_data='contr1')
        bt2=types.InlineKeyboardButton('Контракт №2',callback_data='contr2')
        markup.row(bt1,bt2)
        bt3=types.InlineKeyboardButton('Контракт №3', callback_data='contr3')
        bt4=types.InlineKeyboardButton('Контракт №4', callback_data='contr4')
        markup.row(bt3,bt4)
        bot.send_message(callback_query.message.chat.id,'Выберите контракт',reply_markup=markup)
        bot.answer_callback_query(callback_query.id)
    if callback_query.data=='contr1':
        markup=types.InlineKeyboardMarkup()
        for n in range(1,len(set(names))+1):
            markup.add(types.InlineKeyboardButton(f'{list(g(names))[n-1]}',callback_data='m'+str(n)))
        bot.send_message(callback_query.from_user.id,'Сотрудники к контракту №1',reply_markup=markup)
        bot.answer_callback_query(callback_query.id)
    for n in range(1,len(set(names))+1):
        if callback_query.data=='m'+str(n) :
            print(users)
            p=users[n-1]
            print(p)
            # bot.send_message(p,'Файлы для контракта №1')
            # bot.forward_message(p, -1002440265368, 70)
            # bot.answer_callback_query(callback_query.id)
            contracts1.append(p)
            bot.answer_callback_query(callback_query.id)
        else:
            continue



    if callback_query.data == 'contr2':
        markup = types.InlineKeyboardMarkup()
        for m in range(1, len(set(names)) + 1):
            markup.add(types.InlineKeyboardButton(f'{list(g(names))[m - 1]}', callback_data='x'+str(m)))
        bot.send_message(callback_query.from_user.id, 'Сотрудники к контракту №2', reply_markup=markup)
        bot.answer_callback_query(callback_query.id)
        # for callback_query.message.chat.id in users:
    for m in range(1, len(set(names)) + 1):
        if callback_query.data == 'x'+str(m) :
            print(users)
            p = users[m - 1]
            print(p)
            # bot.send_message(p, 'Файлы для контракта №2')
            # bot.forward_message(p, -1002440265368, 71)
            # bot.answer_callback_query(callback_query.id)
            contracts2.append(p)
            bot.answer_callback_query(callback_query.id)
        else:
            continue

    if callback_query.data == 'contr3':
        markup = types.InlineKeyboardMarkup()
        for q in range(1, len(set(names)) + 1):
            markup.add(types.InlineKeyboardButton(f'{list(g(names))[q - 1]}', callback_data='y'+str(q)))
        bot.send_message(callback_query.from_user.id, 'Сотрудники к контракту №3', reply_markup=markup)
        bot.answer_callback_query(callback_query.id)
        # for callback_query.message.chat.id in users:
    for q in range(1, len(set(names)) + 1):
        if callback_query.data == 'y'+str(q)  :
            print(users)
            p = users[q - 1]
            print(p)
            # bot.send_message(p, 'Файлы для контракта №3')
            # bot.forward_message(p, -1002440265368, 72)
            # bot.answer_callback_query(callback_query.id)
            contracts3.append(p)
            bot.answer_callback_query(callback_query.id)
        else:
            continue


    if callback_query.data == 'contr4':
        markup = types.InlineKeyboardMarkup()
        for t in range(1, len(set(names)) + 1):
            markup.add(types.InlineKeyboardButton(f'{list(g(names))[t - 1]}', callback_data='j'+str(t)))
        bot.send_message(callback_query.from_user.id, 'Сотрудники к контракту №4', reply_markup=markup)
        bot.answer_callback_query(callback_query.id)
        # for callback_query.message.chat.id in users:
    for t in range(1, len(set(names)) + 1):
        if callback_query.data == 'j'+str(t) :
            print(users)
            p = users[t - 1]
            print(p)
            # bot.send_message(p, 'Файлы для контракта №4')
            # bot.forward_message(p, -1002440265368, 73)
            # bot.answer_callback_query(callback_query.id)

            contracts4.append(p)
            bot.answer_callback_query(callback_query.id)
        else:
            continue




    print('contracts 1 =', contracts1)
    print('contracts 2 =', contracts2)
    print('contracts 3 =', contracts3)
    print('contracts 4 =', contracts4)
    if callback_query.data=='viewdoc':
        markup=types.InlineKeyboardMarkup()
        if callback_query.message.chat.id in contracts1:
            markup.add(types.InlineKeyboardButton('Контракт №1',callback_data='co1'))
        if callback_query.message.chat.id in contracts2:
            markup.add(types.InlineKeyboardButton('Контракт №2',callback_data='co2'))
        if callback_query.message.chat.id in contracts3:
            markup.add(types.InlineKeyboardButton('Контракт №3',callback_data='co3'))
        if callback_query.message.chat.id in contracts4:
            markup.add(types.InlineKeyboardButton('Контракт №4',callback_data='co4'))
        bot.send_message(callback_query.message.chat.id,'Доступные контракты',reply_markup=markup)
        bot.answer_callback_query(callback_query.id)



    if callback_query.data=='co1':
        if callback_query.from_user.id in users:
            bot.send_message(callback_query.message.chat.id,'Файлы для контракта №1')
            bot.forward_message(callback_query.message.chat.id, settings.ID_OF_CHAT, 70)
            bot.answer_callback_query(callback_query.id)
        else:
            bot.send_message(callback_query.message.chat.id,'Вы не обладаете правами доступа к контракту')
            bot.answer_callback_query(callback_query.id)
    if callback_query.data=='co2':
        if callback_query.from_user.id in users:
            bot.send_message(callback_query.message.chat.id,'Файлы для контракта №2')
            bot.forward_message(callback_query.message.chat.id, settings.ID_OF_CHAT, 71)
            bot.answer_callback_query(callback_query.id)
        else:
            bot.send_message(callback_query.message.chat.id,'Вы не обладаете правами доступа к контракту')
            bot.answer_callback_query(callback_query.id)
    if callback_query.data=='co3':
        if callback_query.from_user.id in users:
            bot.send_message(callback_query.message.chat.id,'Файлы для контракта №3')
            bot.forward_message(callback_query.message.chat.id, settings.ID_OF_CHAT, 72)
            bot.answer_callback_query(callback_query.id)
        else:
            bot.send_message(callback_query.message.chat.id,'Вы не обладаете правами доступа к контракту')
            bot.answer_callback_query(callback_query.id)
    if callback_query.data=='co4':
        if callback_query.from_user.id in users:
            bot.send_message(callback_query.message.chat.id,'Файлы для контракта №4')
            bot.forward_message(callback_query.message.chat.id, settings.ID_OF_CHAT, 73)
            bot.answer_callback_query(callback_query.id)
        else:
            bot.send_message(callback_query.message.chat.id,'Вы не обладаете правами доступа к контракту')
            bot.answer_callback_query(callback_query.id)


    if callback_query.data == 'deleter':
        markup = types.InlineKeyboardMarkup()
        for n in range(1, len(set(names)) + 1):
            markup.add(types.InlineKeyboardButton(f'{list(set(names))[n - 1]}', callback_data='neas' + str(n)))
        bot.send_message(callback_query.from_user.id, 'Сотрудники', reply_markup=markup)
        bot.answer_callback_query(callback_query.id)
    for n in range(1, len(set(names)) + 1):
        if callback_query.data == 'neas' + str(n):
            print(users)
            p = users[n - 1]
            print(p)
            # bot.send_message(p,'Файлы для контракта №1')
            # bot.forward_message(p, -1002440265368, 70)
            # bot.answer_callback_query(callback_query.id)
            users.remove(users[n - 1])
            names.remove(names[n - 1])
            bot.answer_callback_query(callback_query.id)

        else:
            continue















































bot.polling(none_stop=True)