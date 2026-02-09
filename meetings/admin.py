from django.contrib import admin
from django.contrib.admin import ModelAdmin

# Register your models here.
from meetings.models import Meeting, Room

admin.site.register(Meeting)
admin.site.register(Room)

'''
@admin.register(Meeting)
class MeetingAdmin(ModelAdmin):
    model = Meeting
    list_display = ("id", "title", "date", "start_time", "room")
    ordering = ("date", "start_time")
    search_fields = ("title",)

    #can use this to customize the admin interface, useful and powerful. 
'''