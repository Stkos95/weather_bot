from environs import Env
import json


env=Env()
env.read_env()

token=env.str('TOKEN')
admins=env.list('ADMINS')


'''Для погоды'''
API_KEY =''
link = f'http://api.openweathermap.org/data/2.5/'
lang = 'ru'
link_city='http://api.openweathermap.org/geo/1.0/direct'

