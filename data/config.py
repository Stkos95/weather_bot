from environs import Env
import json


env=Env()
env.read_env()

token=env.str('TOKEN')
admins=env.list('ADMINS')


'''Для погоды'''
API_KEY ='a229bc174cb34d7d123d5d74973678be'
link = f'http://api.openweathermap.org/data/2.5/'
lang = 'ru'
link_city='http://api.openweathermap.org/geo/1.0/direct'

'''Для викторины'''
token_quiz=env.str('TOKEN_QUIZ')
link_quiz=env.str("LINK_QUIZ")


