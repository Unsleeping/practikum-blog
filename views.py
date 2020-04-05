from django.http import HttpResponse


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
