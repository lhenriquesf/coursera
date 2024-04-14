from django.urls import path
from .views import MenuItemsView, SingleMenuItemView

urlpatterns = [
    path('menu-items',MenuItemsView.as_view()),
    path('menu-items/<int:pk>',SingleMenuItemView.as_view()),
]