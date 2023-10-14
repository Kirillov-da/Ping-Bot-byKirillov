from ping3 import ping
import config
import telebot
import time

bot = telebot.TeleBot(config.token)

a=1
i=0
j=0
k=0
while b==1:
 time.sleep(120)

 if (ping('185.216.83.217') is None):
   i=1
 else:
  print (i,j)
  if(i==1 and j==1):
   i=0
   j=0
   print('Сервер Активен')
   bot.send_message(390637743, 'Сервер Активен')
 if (i==1 and j!=1):
    print('Сервер Упал, поднимай!')
    bot.send_message(390637743, 'Сервер Упал, поднимай!')
    if i==1:
        j=1
 


    
