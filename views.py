from django.http import HttpResponse

articles_list = [
    [1, "Айви Яптанго", 2020, "Самые шикарные парочки знаменитостей 2019 года", ["красота", "гороскопы"]],
    [2, "Лео Месси", 2014, "Un Abrazo a Todos", ["лайфстайл", "недвижимость"]],
    [3, "Гэри Паска", 2016, "Продаётся дом в Южной Флориде за $2,695", ["недвижимость", "коучинг", "howto"]],
    [4, "Роби Тобинсон", 1967, "7 лет я применял этот трюк и назад пути нет", ["лайфхак", "коучинг", "howto"]],
    [5, "Металлий Вутко", 2017, "Let Me Speak From My Heart", ["футбол", "допинг"]],
    [6, "Роби Тобинсон", 1977, "Беспроигрышная древнеримская техника обольщения", ["отношения", "история", "howto"]],
    [7, "Роби Тобинсон", 2022, "3 способа установить девайс от храпа", ["здоровье", "коучинг", "howto"]],
    [8, "Роби Тобинсон", 1975, "Интимная проблема, которой втайне озабочены все ваши друзья",
     ["отношения", "здоровье", "howto"]],
    [9, "Elina Shake", 2008, "Представления, основанные на классах", ["python", "howto", "лайфхак"]],
    [10, "Бен Франклин", 1753, "Электрические стодолларовые купюры", ["фондовая биржа", "рынки", "электричество"]],
    [11, "Роби Тобинсон", 2012, "5 забавных Django Apps, о которых говорят все", ["django", "IT", "howto"]],
    [12, "Металлий Вутко", 2017, "No Problems, No Criminality", ["допинг", "недвижимость"]],
    [13, "Роби Тобинсон", 1987, "7 способов до смерти напугать своего босса в пятницу 13-го",
     ["работа", "мистика", "howto"]],
    [14, "Твентин Карантино", 2007, "Четыре сервера", ["кино", "django", "мистика"]],
]


def index(request):
    # создаём объект типа HttpResponse
    resp = HttpResponse('<h1>Главная страница проекта My Praktikum Blog</h1>')
    # и возвращаем его
    return resp


# в функции generate_html() 
# оформим перечень статей в виде html-списка
def generate_html(articles):
    if len(articles) == 0:
        return '<h1>My Praktikum Blog: здесь нет ни одной статьи!</h1>'
    else:
        base_html = '<h1>My Praktikum Blog: лента статей</h1> <ul>'
        for article in articles:
            list_item = f'<li><ul><li><strong>{article[3]}</strong></li><li>автор: {article[1]}</li>' \
                        f'<li>год: {article[2]}</li><li>теги: {", ".join(article[4])}</li></ul></li>'
            base_html += list_item
        base_html += '</ul>'
        return base_html


def dashboard(request):
    # вызовите функцию generate_html()
    # и передайте ей список статей в качестве аргумента.
    # результат сохраните в переменную beautiful_html
    beautiful_html = generate_html(articles_list)
    # верните обработанный список статей 
    return HttpResponse(beautiful_html)

def index(request):
    html = '''<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <title>My Praktikum Blog</title>
</head>
<body>
    <h1>Главная страница нашего проекта</h1>
    <p>Привет, <b>Unsleeping</b>!</p>
    <p>Начинаем работать с Django-тренажёром.</p>
</body>
</html>'''

    # создаём объект типа HttpResponse
    resp = HttpResponse(html)

    # и возвращаем его
    return resp


# для url accounts/sign-up
def sign_up(request): 
    return HttpResponse('<h1>Страница регистрации</h1>')

# для url accounts/sign-in
def sign_in(request): 
    return HttpResponse('<h1>Страница авторизации</h1>')

# для url accounts/my-account
def my_account(request): 
    return HttpResponse('<h1>Данные вашего аккаунта</h1>')
