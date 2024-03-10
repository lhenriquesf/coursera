from django.urls import path
from .views import ShowFormView, BookingFormView, IndexView, AboutView, MenuView, HomeView, MenuByIdView

urlpatterns = [
    path('show_form/', ShowFormView.as_view(), name='show_form_view'),
    path('booking/', BookingFormView.as_view(), name='booking'),
    path('index/<str:name>/', IndexView.as_view(), name='index'),
    path('about/', AboutView.as_view(), name='about'),
    path('menu/', MenuView.as_view(), name='menu'),
    path('', HomeView.as_view(), name='home'),
    path('menu_card/', MenuByIdView.as_view(), name='menu_by_id'),
]