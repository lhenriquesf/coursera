from django.urls import path
from . import views

urlpatterns = [
    path('',views.show_form_view, name='show_form_view'),
    path('booking/',views.booking_form,name='booking_form'),
    path('index/<str:name>', views.index, name='index'),
    path('about/',views.about,name='about'),
    path('menu/',views.menu),
    path('menu_card/',views.menu_by_id),
]