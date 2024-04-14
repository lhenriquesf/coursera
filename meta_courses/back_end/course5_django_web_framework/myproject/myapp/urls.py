from django.urls import path
from .views import ShowFormView, BookingFormView, AboutView, MenuView, HomeView, MenuByIdView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('show_form/', ShowFormView.as_view(), name='show_form_view'),
    path('booking/', BookingFormView.as_view(), name='booking'),
    path('about/', AboutView.as_view(), name='about'),
    path('menu/', MenuView.as_view(), name='menu'),
    path('menu_item/', MenuByIdView.as_view(), name='menu_by_id'),
]