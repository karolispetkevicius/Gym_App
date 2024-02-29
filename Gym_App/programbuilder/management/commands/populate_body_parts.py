from django.core.management.base import BaseCommand
from models import BodyPart

class Command(BaseCommand):
    help = 'Populates BodyPart objects with the bodyparts'

    def handle(self, *args, **kwargs):
        body_parts = ['Chest', 'Shoulders', 'Biceps', 'Triceps', 'Legs', 'Back', 'Glutes', 'Abs', 'Calves']
        
        for body_part in body_parts:
            BodyPart.objects.get_or_create(body_part=body_part)

        self.stdout.write(self.style.SUCCESS('Successfully populated BodyPart objects'))