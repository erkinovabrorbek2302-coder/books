# my_app.urls
from django.urls import path
from .views import first_view,pages
from django.urls import path

urlpatterns = [
    path('',first_view, name='first_page'),
    path('pages/<str:page>',pages, name='pages'),
    path('books/', first_view, name='books_page'),
]