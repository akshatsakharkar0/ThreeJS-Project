
from django.contrib import admin
from django.urls import path
from .views import mainpage

app_name = 'Home'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',mainpage,name='mainpage'),
]
