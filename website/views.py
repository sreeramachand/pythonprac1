from django.shortcuts import render
from django.http import HttpResponse

from meetings.models import Meeting

# Create your views here.
def welcome(request):
    #added a filter where request user id must match meetings displayed
    if request.user.is_authenticated:
        context = {"message": "Here's a message to you...", 
                                                    "meetings": Meeting.objects.filter(participants__exact=request.user.id)}
    else:
        context = {}
    return render(request, "website/welcome.html", context)

def about(request):
    return HttpResponse("This is an 'About' Page.")