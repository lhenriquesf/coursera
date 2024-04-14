
# from django.http import HttpResponse
from django.shortcuts import render
from .forms import BookingForm
from .models import Menu
from django.views import View

# Create your views here.
class HomeView(View):
    template_name = 'index.html'

    def get(self, request):
        return render(request, self.template_name)



class AboutView(View):
    template_name = 'about.html'

    def get(self, request):
        return render(request, self.template_name)
    


class BookView(View):
    template_name = 'book.html'

    def get(self, request):
        form = BookingForm()
        context = {'form':form}
        return render(request, self.template_name, context)
    
    def post(self, request):
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
        context = {'form':form}
        return render(request, self.template_name, context)
        


class MenuView(View):
    template_name = 'menu.html'

    def get(self,request):
        menu_data = Menu.objects.all()
        main_data = {'menu':menu_data}
        return render(request, self.template_name, main_data)



class DisplayMenuItemsView(View):
    template_name = 'menu_item.html'

    def get(self,request,pk=None):
        if pk:
            menu_item = Menu.objects.get(pk=pk)
        else:
            menu_item = ''
        menu_dict = {'menu_item':menu_item}

        return render(request, self.template_name, menu_dict)