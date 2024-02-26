from django.urls import path
from . import views

urlpatterns = [
    path('',views.show_form_view, name='show_form_view'),
    path('booking/',views.booking_form,name='booking_form')
]