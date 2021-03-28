from datetime import datetime
from django.shortcuts import render


def all_rooms(request):
    all_rooms = models.Room.objects.all()
    return render(request, "all_rooms.html", context={"rooms": all_rooms})
