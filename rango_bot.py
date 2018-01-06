#!/usr/bin/python
#coding: utf-8
#creator: laps3
#contact: Telegram:@lapselapse
import telepot
import time
from datetime import datetime
import base64
import os
import sys
from selenium import webdriver
import shodan
from datetime import timedelta

os.system("clear")
now = datetime.now()
api_key = ''
####Colors####
cyanClaro = "\033[1;36m"
vermelho = "\33[31m"

bot = telepot.Bot("")

def decode_and_decode(browser, string, type):
    browser.find_element_by_class_name('m1write').send_keys(string)
    browser.find_element_by_name(type).click() #encode or decode
    value = browser.find_element_by_class_name('m1write').get_attribute('value')
    browser.quit()
    return value

def handle(msg):

    uid = msg['from']['id']
    pnome = msg['from']['first_name']#Primeiro nome
    chat_id = msg['chat']['id']#id do grupo
    chat_type = msg['chat']['type']
    id_criador = str()
    nick = msg['from']['username']#username, @username
    msgid = msg['message_id']#id da msg

    ####search####
#   bas64 = msg.get('text').split()
    ###time###
    dia = str(now.day)
    mes = str(now.month)
    ano = str(now.year)
    hora = str(now.hour)
    minut = str(now.minute)
    segundo = str(now.second)

    #Codigo - log do comandos
    users = open('users-register.txt', 'a')
    log = open('log_comands.txt', 'a')


    content_type, chat_type, chat_id = telepot.glance(msg)
    if msg.get('text'):
        texto = msg['text']
        ntexto = texto.split(' ')

        if texto == '/start':
            if chat_type == 'private':
                bot.sendMessage(chat_id, "RangoDecoder ao seu dispor!", reply_to_message_id=msgid)
                print(nick, " started bot in private")
                print("")
                users.write(str("log [" + dia + "/" + mes + "/" + ano + "][" + hora + ":" + minut + ":" + segundo + "]"))
                users.write(str(" | Username: " + nick + " | ID: " + str(uid) + " | Comando usado: " + texto + " | Chat: " + chat_type + "\n"))
                users.close()
                print('[+]', nick + " Started")
            else:
                bot.sendMessage(chat_id,"Iniciaremos uma conversa agora!", reply_to_message_id=True)
                print(cyanClaro + "In group", nick, "started the bot")
                print("")
        elif texto == '/id':
            bot.sendMessage(chat_id, uid, reply_to_message_id=msgid)
            log.write(str("log [" + dia + "/" + mes + "/" + ano + "][" + hora + ":" + minut + ":" + segundo + "]"))
            log.write(str(" | Username: " + nick + " | ID: " + str(uid) + " | Comando usado: " + texto + " | ChatType: " + chat_type + " | Chat ID: " + str(chat_id) + "\n"))
            log.close()
            print('[+]', nick + "Log sucessfully")
            print("")
        elif texto == '/functions':
            bot.sendMessage(chat_id, "Functions of criptography: Base64 // atom128 // megan35 // tripo5 // arabica2", reply_to_message_id=msgid)
            log.write(str("log [" + dia + "/" + mes + "/" + ano + "][" + hora + ":" + minut + ":" + segundo + "]"))
            log.write(str(" | Username: " + nick + " | ID: " + str(uid) + " | Comando usado: " + texto + " | ChatType: " + chat_type + " | Chat ID: " + str(chat_id) + "\n"))
            log.close()
            print(cyanClaro + '[+]', nick, " read the functions")
            print(cyanClaro + '[+] Saved in logs.txt')
            print("")
        elif texto == '/help':
            bot.sendMessage(chat_id, "The objective is criptography but has many tools!", reply_to_message_id=msgid)
            log.write(str("log [" + dia + "/" + mes + "/" + ano + "][" + hora + ":" + minut + ":" + segundo + "]"))
            log.write(str(" | Username: " + nick + " | ID: " + str(uid) + " | Comando usado: " + texto + " | ChatType: " + chat_type + " | Chat ID: " + str(chat_id) + "\n"))
            log.close()
            print(cyanClaro + '[+]', nick, "read help")
            print(cyanClaro + '[+] Saved in logs.txt')
            print("")
        elif msg.get('text').startswith('/base64decode'):
            search = msg.get('text').split()
            print(cyanClaro + '[+]', nick, "used the decrypt for this", search[1])
            baba = base64.b64decode(' '.join(search[1:]))
            bot.sendMessage(chat_id, f"Result: {baba}")
            print(cyanClaro + '[+] Decode sucessfully')
            log.write(str("log [" + dia + "/" + mes + "/" + ano + "][" + hora + ":" + minut + ":" + segundo + "]"))
            log.write(str(" | Username: " + nick + " | ID: " + str(uid) + " | Comando usado: " + texto + " | ChatType: " + chat_type + " | Chat ID: " + str(chat_id) + "\n"))
            log.close()
            print(cyanClaro + '[+] Saved in logs.txt')
            print("")
        elif texto == '/commands':
            bot.sendMessage(chat_id, '/base64decode\n/base64encode\n/atom128encode\n/atom128decode\n/megan35encode\n/megan35decode\n/tripo5encode\n/tripo5decode\n/arabica2encode\n/arabica2decode', reply_to_message_id=msgid)
            print(cyanClaro + "[+] Commands printed for ", nick)
            log.write(str("log [" + dia + "/" + mes + "/" + ano + "][" + hora + ":" + minut + ":" + segundo + "]"))
            log.write(str(" | Username: " + nick + " | ID: " + str(uid) + " | Comando usado: " + texto + " | ChatType: " + chat_type + " | Chat ID: " + str(chat_id) + "\n"))
            log.close()
            print(cyanClaro + '[+] Saved in logs.txt')
            print("")
        elif msg.get('text').startswith('/base64encode'):
            search = msg.get('text').split()
            print(search)
            print(cyanClaro + '[+] Encoding this: ', search[1])
            encoded = base64.b64encode(' '.join(search[1:]).encode('utf-8'))
            bot.sendMessage(chat_id, f"Result: {encoded}", reply_to_message_id=msgid)
            print(cyanClaro + '[+] Saved in logs.txt')
            print('')       
        elif msg.get('text').startswith('/shodan'):
            searc = msg.get('text').split()
            api = shodan.Shodan(api_key)
            print(cyanClaro + '[+] Search shodan started')
            try:
                results = api.search(''.join(searc[1]))
                print(results['total'])
                for result in results['matches']:
                    print(result['ip_str'])
                    bot.sendMessage(chat_id, f"IP: {result['ip_str']}", reply_to_message_id=msgid)
                    print(result['data'])
                    bot.sendMessage(chat_id, f"Data: {result['data']}", reply_to_message_id=msgid)
                    break
            except shodan.APIError:
                    print('Error')
        elif texto == '/uptime':
            if (uid == ):
                with open('/proc/uptime', 'r') as f:
                    uptime_seconds = float(f.readline().split()[0])
                    uptime_string = str(timedelta(seconds = uptime_seconds))
                bot.sendMessage(chat_id, uptime_string, reply_to_message_id=msgid)
                print('[*] Uptime printed')
            else:
                print(uid, 'não tem permissão')
                bot.sendMessage(chat_id, "Você não tem permissão!")          
        elif msg['text'][0:8] in ('/megan35', '/atom128') or ('/tripo5', '/arabica2'):
            string = msg.get('text').split()
            config = {
                '/megan35encode' : {'type' : 'encode', 'string': ' '.join(string[1:]), 'url': 'http://temp.crypo.com/megan35c.htm'}, 
                '/megan35decode' : {'type' : 'decode', 'string': ' '.join(string[1:]), 'url': 'http://temp.crypo.com/megan35c.htm'},
                '/atom128encode' : {'type' : 'encode', 'string': ' '.join(string[1:]), 'url': 'http://temp.crypo.com/atom128c.htm'}, 
                '/atom128decode' : {'type' : 'decode', 'string': ' '.join(string[1:]), 'url': 'http://temp.crypo.com/atom128c.htm'},
                '/tripo5encode' : {'type' : 'encode', 'string': ' '.join(string[1:]), 'url': 'http://temp.crypo.com/tripo5c.htm'},
                '/tripo5decode' : {'type' : 'decode', 'string': ' '.join(string[1:]), 'url': 'http://temp.crypo.com/tripo5c.htm'},
                '/arabica2encode' : {'type' : 'encode', 'string': ' '.join(string[1:]), 'url': 'http://temp.crypo.com/arabica-2rs.htm'},
                '/arabica2decode' : {'type' : 'decode', 'string': ' '.join(string[1:]), 'url': 'http://temp.crypo.com/arabica-2rs.htm'}
                
            }

            browser = webdriver.PhantomJS()
            browser.get(config[string[0]]['url'])
            del config[string[0]]['url']
            msg = decode_and_decode(browser, **config[string[0]])
            bot.sendMessage(chat_id, f"Result: {msg}", reply_to_message_id=msgid)
            print(cyanClaro + '[+] Decode or encode Success')
        elif texto == '/ban':
            bot.kickChatMember(uid, reply_to_message_id=msgid)
            bot.sendMessage(chat_id, 'User banned') 
    elif msg.get('new_chat_member'):
        print('[+] New user')
        bot.sendMessage(chat_id, 'Wellcome')
    
bot.message_loop(handle)
print(vermelho + '-----Bot Started-----')
while 1:
    pass
