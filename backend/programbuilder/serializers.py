from rest_framework import serializers
from .models import *

class BodyPartSerializer(serializers.ModelSerializer):
    class Meta:
        model = BodyPart
        fields = '__all__'  


class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        exclude = ('body_part', )


class WorkoutProgramSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkoutProgram
        fields = '__all__'


class ProgramDaySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProgramDay
        fields = '__all__'


class ExerciseInDaySerializer(serializers.ModelSerializer):
    class Meta:
        model = ExerciseInDay
        fields = '__all__'