from django.contrib import admin
from .models import Menu, Drinks, DrinksCategory, Logger, Booking, Employees

# Register your models here.
admin.site.register(DrinksCategory)
admin.site.register(Drinks)
admin.site.register(Menu)
admin.site.register(Logger)
admin.site.register(Booking)
admin.site.register(Employees)


