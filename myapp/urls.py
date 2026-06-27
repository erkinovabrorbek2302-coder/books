# from django.urls import path
# from my_app import admin
# # from .views import main,person_list
# from . import views
# urlpatterns = [
#     # path('', main, name='main'),
#     # path('person_list/',person_list, name='person_list'),
#     path('register/', views.register_view, name='register'),
# ]
from django.urls import path
from . import views

urlpatterns = [
    # 1. Bosh sahifa (/) -> registratsiya formasini ko'rsatadi
    path('', views.register_view, name='home'),

    # 2. Forma jo'natiladigan manzil (register/ -> ma'lumotlar qabul qilinadi)
    path('register/', views.register_view, name='register'),
]