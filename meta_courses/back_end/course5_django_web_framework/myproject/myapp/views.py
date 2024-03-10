from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .forms import LogForm, BookingForm
from .models import Menu

# Create your views here.

class ShowFormView(View):
    template_name = 'form.html'

    def get(self, request):
        form = LogForm()
        context = {'form': form}
        return render(request, self.template_name, context)


    def post(self, request):
        form = LogForm(request.POST)
        if form.is_valid():
            form.save()
        context = {'form': form}
        return render(request, self.template_name, context)
    


class BookingFormView(View):
    template_name = 'booking.html'

    def get(self, request):
        form = BookingForm()
        context = {'form': form}
        return render(request, self.template_name, context)


    def post(self, request):
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
        context = {'form': form}
        return render(request, self.template_name, context)



class HomeView(View):
    template_name = 'home.html'

    def get(self, request):
        return render(request, self.template_name)



class AboutView(View):
    template_name = 'about.html'

    def get(self, request):
        return render(request, self.template_name)



class MenuView(View):
    template_name = 'menu.html'

    def get(self, request):
        return render(request, self.template_name)



class MenuByIdView(View):
    template_name = 'menu_card.html'

    def get(self, request):
        newmenu = Menu.objects.all()
        newmenu_dict = {'menu': newmenu}
        return render(request, self.template_name, newmenu_dict)



class IndexView(View):
    def get(self, request, name):
        return HttpResponse('<h1>Hello {}</h1>'.format(name))