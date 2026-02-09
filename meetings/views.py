from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect
# Create your views here.
from meetings.models import Meeting, Room
from django.forms import modelform_factory

def detail(request, id):
    meeting = get_object_or_404(Meeting, pk=id)
    return render(request, "meetings/detail.html", {"meeting": meeting}) 

def rooms_list(request):
    return render(request, "meetings/rooms_list.html", {"rooms": Room.objects.all()})


MeetingForm = modelform_factory(Meeting, exclude=[])

def new(request):
    if request.method == "POST":
        #form has been submitted, process data
        form = MeetingForm(request.POST)
        if form.is_valid():
            form.save() #saves in the database
            return redirect("welcome")
        else:
            form = MeetingForm()
            return render(request, "meetings/new.html", {"form": form})

    form = MeetingForm()
    return render(request, "meetings/new.html", {"form": form,})

def edit(request, id):
    meeting = get_object_or_404(Meeting, pk=id)
    if request.method == "POST":
        form = MeetingForm(request.POST, instance=meeting)
        if form.is_valid():
            form.save()
            return redirect("detail", id)
    else:
        form = MeetingForm(request.POST, instance=meeting)
    return render(request, "meetings/edit.html", {"form": form})

def delete(request, id):
    meeting = get_object_or_404(Meeting, pk=id)
    if request.method == "POST":
        # Form is only shown to ask for configuration
        # When we get a POST, we know we can go ahead and delete
        meeting.delete()
        return redirect('welcome')
    else:
        return render(request, "meetings/confirm_delete.html", {"meeting": meeting,})