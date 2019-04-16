from django.contrib import admin
from django.urls import path, re_path, include
from . import views

urlpatterns = [
    path('city/', views.List_cities.as_view()),
    path('city/<int:city_id>/street/', views.City_street.as_view()),
    # path('shop/', views.create_shop),
    path('shop/', views.Shop_work.as_view()),
]
