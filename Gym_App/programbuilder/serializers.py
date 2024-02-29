from rest_framework import serializers
from models import BodyPart, Exercise, Day, WorkoutProgram, ProgramDay, ExerciseInProgram

class BodyPartSerializer(serializers.ModelSerializer):
    class Meta:
        model = BodyPart
        fields = '__all__'  # You can specify specific fields if needed


class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = '__all__'


class DaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Day
        fields = '__all__'


class WorkoutProgramSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkoutProgram
        fields = '__all__'


class ProgramDaySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProgramDay
        fields = '__all__'


class ExerciseInProgramSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExerciseInProgram
        fields = '__all__'