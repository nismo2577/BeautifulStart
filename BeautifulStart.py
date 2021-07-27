from datetime import datetime
from pyowm.owm import OWM
from colorama import init, Fore, Style

import config

init()

# Getting local time
now_datetime = datetime.now()
parsed_time = f'{"0" + str(now_datetime.hour) if now_datetime.hour < 10 else now_datetime.hour}:' \
              f'{"0" + str(now_datetime.minute) if now_datetime.minute < 10 else now_datetime.minute}'

# Getting local date
weekdays = ('Mon', 'Tue', 'Wen', 'Thu', 'Fri', 'Sat', 'Sun')
parsed_date = f'{weekdays[now_datetime.isoweekday()]} ' \
                  f'{"0" + str(now_datetime.day) if now_datetime.day < 10 else now_datetime.day}'

# Getting weather
owm = OWM(config.API_KEY)
weather_manager = owm.weather_manager()
observation = weather_manager.weather_at_place(config.CITY)

weather_statuses = {
    'Rain': '🌧',
    'Clouds': '☁️',
    'Snow': '❄',
    'Clear': '☀'
}
parsed_weather = f'{round(observation.weather.temperature("celsius")["temp"], 1)}°C ' \
                 f'{weather_statuses.get(observation.weather.status, "🌎")}'

# Configuration banner
banner = fr"""{Style.BRIGHT}
--------------------------------
|  {Fore.YELLOW}_   _      _ _{Fore.RESET}  | {parsed_date}    |     
| {Fore.YELLOW}| | | |    | | |{Fore.RESET} | {parsed_weather}  |     
| {Fore.YELLOW}| |_| | ___| | |{Fore.RESET} ------------| 
| {Fore.YELLOW}|  _  |/ _ \ | |/ _ \{Fore.RESET}        |
| {Fore.YELLOW}| | | |  __/ | | (_) |{Fore.RESET}       |
| {Fore.YELLOW}\_| |_/\___|_|_|\___/{Fore.RESET}        |
--------------------------------{Style.RESET_ALL}
"""
print(banner)
