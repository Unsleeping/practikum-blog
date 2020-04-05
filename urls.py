# импортируем функцию для проверки запрошенных URL
from django.urls import path  
# импортируем все три файла с view-функциями из разных директорий
from accounts import views as acc_views
from articles import views as art_views 
from . import views

urlpatterns = [
     # правила для сопоставления шаблонов URL и функций
     path('', views.index),
     path('articles/dashboard', art_views.dashboard),
     path('accounts/sign-up', acc_views.sign_up),
     path('accounts/sign-in', acc_views.sign_in),
     path('accounts/my-account', acc_views.my_account)
]
