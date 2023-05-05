from django.urls import path
from . import views

urlpatterns=[
    path('', views.home, name='home'), 
    path('book/<int:id>/', views.home_detail, name='home_detail'), 
    path('book_list/<int:id>/', views.book, name='book'), 
]