from django.db import models
from django.utils import timezone
from django.contrib.postgres.fields import ArrayField
from django.contrib.auth.models import User





class BodyPart(models.Model):
    BODY_PARTS = [
        ('Chest', 'Chest'),
        ('Shoulders', 'Shoulders'),
        ('Bicep', 'Bicep'),
        ('Triceps', 'Triceps'),
        ('Legs', 'Legs'),
        ('Back', 'Back'),
        ('Glutes', 'Glutes'),
        ('Abs', 'Abs'),
        ('Calves', 'Calves')
    ]

    body_part = models.CharField(max_length=50, choices=BODY_PARTS, unique=True)

    def __str__(self):
        return self.body_part


class Exercise(models.Model):
    exercise = models.CharField(max_length=50)
    body_part = models.ForeignKey(BodyPart, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.exercise
    


class Day(models.Model):
    DAY_CHOICES = [
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
        ('Saturday', 'Saturday'),
        ('Sunday', 'Sunday'),
    ]

    day_of_week = models.CharField(max_length=20, choices=DAY_CHOICES)

    def __str__(self):
        return self.day_of_week




class WorkoutProgram(models.Model):   
    name = models.CharField(max_length=100, null=True)
    days = models.ManyToManyField(Day, through='ProgramDay')



class ProgramDay(models.Model):
    program = models.ForeignKey(WorkoutProgram, on_delete=models.CASCADE)
    day = models.ForeignKey(Day, on_delete=models.CASCADE)
    order = models.PositiveIntegerField(default=1)

    class Meta:
        unique_together=['program','order']

    def __str__(self):
        return f"{self.program.name} - Day {self.order}"


class ExerciseInProgram(models.Model):
    program_day = models.ForeignKey(ProgramDay, on_delete=models.CASCADE)
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    sets = models.PositiveIntegerField()
    reps = models.PositiveIntegerField()
    order = models.PositiveBigIntegerField(default=1)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.exercise} ({self.program_day})"


