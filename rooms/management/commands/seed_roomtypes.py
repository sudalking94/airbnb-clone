from django.core.management.base import BaseCommand
from rooms.models import RoomType

class Command(BaseCommand):
    help = "This command creates room types"

    def handle(self, *args, **options):
        roomtypes = [
            "Single",
            "Double",
            "Triple",
            "Quad",
            "Queen",
            "King",
            "Twin",
        ]
        for a in roomtypes:
            RoomType.objects.create(name=a)
        self.stdout.write(self.style.SUCCESS("Room typess created!"))