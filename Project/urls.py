from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homePage, name='home'),
    path('delete/<int:id>', deleteBook, name='deleteBook'),
    path('read/<int:id>', readBook, name='readBook'),
]
