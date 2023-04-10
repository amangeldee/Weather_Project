# virtualenv venv
# source venv/bin/activate.fish
# pip install requests
# pip install python-dotenv
# pip freeze > requirements.txt
# Переключить интерпретатор


# #b7fb993143d6b34c000456b6cdbebfc3
# import requests
# from dotenv import load_dotenv
# from os import getenv
# load_dotenv()


# WEATHER_API = getenv('WEATHER_API')
# # city = input('Введите название города: ')
# city = "Almaty"

# url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_API}&units=metric'

# response = requests.get(url)
# data =response.json()

# print(data)

# ish
# virtualenv venv
# source venv/bin/activate.fish
# pip install requests
# pip install python-dotenv
# pip freeze > requirements.txt
# Переключить интерпритатор

# # 4d91b754b37c6feff92c3bcbdeede521

# import requests
# from datetime import datetime
# from os import getenv, system
# from dotenv import load_dotenv
# load_dotenv()

# WEATHER_API = getenv('WEATHER_API')
# def WeatherService(get_city="Almaty", API=WEATHER_API):
#     """Ваш бот-метеоролог мгновенно показывает погоду в любом городе, предоставляя актуальную информацию о температуре воздуха, влажности и вероятности дождя. 
# Это помогает планировать дела эффективнее и быть в курсе погодных событий в режиме реального времени.

# get_city =''
# API = WEATHER_API

# WeatherService(get_city: str, API: StrApiKey) -> str

# """

#     url = f'https://api.openweathermap.org/data/2.5/weather?q={get_city}&appid={API}&units=metric'

#     response = requests.get(url)
#     data = response.json()

#     Pr_Day = {datetime.fromtimestamp(data['sys']['sunset'])}-datetime.fromtimestamp(data['sys']['sunrise'])

#     information = f'''Погода - Nuraiym
#     Страна: {data['sys']['country']}
#     Город:{ data['name']} - {data['weather'][0]['description']} {data['clouds']['all']}%
#     Температура: {data['main']['temp']}°C
#     Ощущается: {data['main']['feels_like']}°C
#     Влажность: {data['main']['humidity']}%
#     Давление воздуха: {data['main']['pressure']}гПа
#     Скорость ветра: {data['wind']['speed']}м/с
#     Направление ветра: {data['wind']['deg']}°
#     Восход солнце: {datetime.fromtimestamp(data['sys']['sunrise'])}
#     Продол-ть дня: {datetime.fromtimestamp(data['sys']['sunset'])}-datetime.fromtimestamp(data['sys']['sunrise'])
#     Закат солнце: {datetime.fromtimestamp(data['sys']['sunset'])}

#     '''
#     system('clear')
#     return information
#     city = input("Введите газвание города: ")
#     city = "Almaty"
#     print(WeatherService(city))

    
# d5bb44d0fa8e39e2339c9019d833d826
import requests
from datetime import datetime
from os import getenv, system
from dotenv import load_dotenv
load_dotenv()

WEATHER_API = getenv('WEATHER_API')

def WeatherService(get_city="Almaty", API=WEATHER_API):
    """
    Ваш бот-метеоролог мгновенно показывает погоду в любом городе, предоставляя актуальную информацию о температуре воздуха, влажности и вероятности дождя. 
    Это помогает планировать дела эффективнее и быть в курсе погодных событий в режиме реального времени.
    
    get_city = 'Almaty'
    API = WEATHER_API

    WeatherService(get_city: str, API: StrApiKey) -> str
    """

    url = f'https://api.openweathermap.org/data/2.5/weather?q={get_city}&appid={API}&units=metric'

    response = requests.get(url)
    data = response.json()

    Pr_Day = datetime.fromtimestamp(data['sys']['sunset']) - datetime.fromtimestamp(data['sys']['sunrise'])
    
    Informations = f"""Погода - Marselle.naz
    Страна: {data["sys"]['country']}
    Город: {data['name']} - {data['weather'][0]['description']} {data['clouds']['all']}%
    Температура: {data['main']['temp']}°C
    Ощушается: {data['main']['feels_like']}°C
    Влажность: {data['main']['humidity']}%
    Давление воздуха: {data['main']['pressure']} гПа
    Скорость ветра: {data['wind']['speed']} м/с
    Направление ветра: {data['wind']['deg']}°
    Восход солнце: {datetime.fromtimestamp(data['sys']['sunrise'])}
    Продол-ть дня: {Pr_Day}
    Закат солнце: {datetime.fromtimestamp(data['sys']['sunset'])}
    """
    system("clear")
    return Informations


city = input("Введите название города: ")
print(WeatherService(city))


