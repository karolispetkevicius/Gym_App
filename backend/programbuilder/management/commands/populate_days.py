from django.core.management.base import BaseCommand
from programbuilder.models import Day

class Command(BaseCommand):
    help = 'Populates Day objects with the days of the week'

    def handle(self, *args, **kwargs):
        days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        
        for day_name in days_of_week:
            Day.objects.get_or_create(day_of_week=day_name)

        self.stdout.write(self.style.SUCCESS('Successfully populated Day objects'))
