from django.urls import path 
# переназовём файлы views.py, чтобы избежать конфликта имён.
# импортируем views.py из папки приложения Articles App:
from articles import views as art_views # ...и будем звать его art_views

# импортируем views.py из папки приложения Accounts App:
from accounts import views as acc_views # ...и будем звать его acc_views 

# импортируем views.py из директории по умолчанию:
from . import views # ...а давать ей специальное имя не будем, оставим views

urlpatterns = [ 
    path('', views.index), 
    path('dashboard', art_views.dashboard), 
    path('sign_up', acc_views.sign_up), 
    path('sign_in', acc_views.sign_in), 
    path('my_account', acc_views.my_account), 
]
