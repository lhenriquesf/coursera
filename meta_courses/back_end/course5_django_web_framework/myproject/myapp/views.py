from django.shortcuts import render
from django.http import HttpResponse
from .forms import LogForm
from .forms import BookingForm

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
    return render(request, 'booking.html',context)

# def get_form_view(request):
#     if request.method == "POST":
#         form = LogForm(request.POST)
#         if form.is_valid():
#             form.save()