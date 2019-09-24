from django.shortcuts import render
from django.http import HttpResponse
from .models import booking
# Create your views here.
def homepage(request):
    return render(request = request,
                  template_name='booksite/home.html',
                  context = {"bookings":booking.objects.all})

def bookform(request):
    return render(request = request,
                  template_name='booksite/bookform.html',
                  context = {"bookings":booking.objects.all})

def bookform(request):
   
    if request.method == 'POST':
        if 'ca' in request.POST:
            if request.POST.get('venue') and request.POST.get('date') and request.POST.get('time'):
                
                a=0
                for reserve in booking.objects.all():
                    if reserve.venue==request.POST.get('venue'):    
                        if reserve.date==request.POST.get('date') :
                            if reserve.time==request.POST.get('time') :
                                a=1
                if a==1 :
                    messages.info(request,'time slot not availabe.')
                else :
                    messages.info(request,'time slot available. plese proceed.')
                
        elif '_book' in request.POST:
            if request.POST.get('venue') and request.POST.get('date') and request.POST.get('time') and request.POST.get('clg') and request.POST.get('email') and request.POST.get('message'):
                Booking=booking()
                Booking.venue= request.POST.get('venue')
                Booking.date= request.POST.get('date')
                Booking.time= request.POST.get('time')
                Booking.college= request.POST.get('clg')
                Booking.email= request.POST.get('email')
                Booking.event_name= request.POST.get('message')
                Booking.save()
                
                return render(request, 'booksite/home.html')
    else:
            return render(request,'booksite/bookform.html')
