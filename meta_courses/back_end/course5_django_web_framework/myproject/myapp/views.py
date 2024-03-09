from django.shortcuts import render
from django.http import HttpResponse
from .forms import LogForm
from .forms import BookingForm
from .models import Menu

# Create your views here.

def show_form_view(request):
    form = LogForm()
    if request.method == 'POST':
        form = LogForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form':form}
    return render(request, 'form.html',context)


def booking_form(request):
    form = BookingForm()
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form':form}
    template_name = 'booking.html'
    return render(request, template_name, context)


def index(request,name):
    return HttpResponse('<h1>Hello {}<h1/>'.format(name))


def about(request):
    content = {'about':'Little Lemon is a family-owned Mediterranean restaurant, focused on traditional recipes served with a modern twist. The chefs draw inspiration from Italian, Greek, and Turkish culture and have a menu of 12–15 items that they rotate seasonally. The restaurant has a rustic and relaxed atmosphere with moderate prices, making it a popular place for a meal any time of the day.'}
    return render(request, 'about.html', content)


def menu(request):
    newmenu={'mains':[
        {'name':'falafel','price':'12'},
        {'name':'shawarma','price':'15'},
        {'name':'gyro','price':'10'},
        {'name':'hummus','price':'5'},
    ]}
    return render(request,'menu.html',newmenu)


def menu_by_id(request):
    newmenu = Menu.objects.all()
    newmenu_dict = {'menu':newmenu}
    return render(request,'menu_card.html',newmenu_dict)