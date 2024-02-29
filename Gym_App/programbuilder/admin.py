from django.contrib import admin
from .models import BodyPart, Exercise, Day, WorkoutProgram, ProgramDay, ExerciseInProgram

admin.site.register(BodyPart)
admin.site.register(Exercise)
admin.site.register(Day)
admin.site.register(WorkoutProgram)
admin.site.register(ProgramDay)
admin.site.register(ExerciseInProgram)