from django.urls import path
from .views import HomeView, AboutView, BookView, MenuView, DisplayMenuItemsView


urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('about/', AboutView.as_view(), name="about"),
    path('book/', BookView.as_view(), name="book"),
    path('menu/',MenuView.as_view(),name="menu"),
    path('menu_item/<int:pk>/',DisplayMenuItemsView.as_view(),name='menu_item'),
]