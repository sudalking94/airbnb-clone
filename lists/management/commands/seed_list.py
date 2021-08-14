import random
from django.core.management.base import BaseCommand
from users import models as user_models
from rooms import models as room_models
from lists import models as list_models

NAME = "lists"


class Command(BaseCommand):

    help = f"This command creates {NAME}"
    
    def handle(self, *args, **options):
        users = user_models.User.objects.all()
        rooms = room_models.Room.objects.all()
        uses_cnt = len(list(users))      
        for user in users:
            list_model = list_models.List.objects.create(user=user, name="My favorite houses")
            to_add = rooms[random.randint(0, 5) : random.randint(6, 30)]
            list_model.rooms.add(*to_add)

        
        self.stdout.write(self.style.SUCCESS(f"{uses_cnt} {NAME} created!"))