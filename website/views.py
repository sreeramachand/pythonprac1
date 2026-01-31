from django.shortcuts import render
from django.http import HttpResponse

from meetings.models import Meeting

# Create your views here.
def welcome(request):
    return render(request, "website/welcome.html", {"message": "Here's a message to you...", 
                                                    "meetings": Meeting.objects.all()})

def about(request):
    return HttpResponse("This is an 'About' Page.")