from django.contrib import admin
from .models import BodyPart, Exercise, WorkoutProgram, ProgramDay, ExerciseInDay

admin.site.register(BodyPart)
admin.site.register(Exercise)
admin.site.register(WorkoutProgram)
admin.site.register(ProgramDay)
admin.site.register(ExerciseInDay)