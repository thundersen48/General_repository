from flask import Blueprint


views = Blueprint(__name__, 'views')
#Определяем корневой каталог
@views.route('/')
def home():
    return 'Привет! Макс'

