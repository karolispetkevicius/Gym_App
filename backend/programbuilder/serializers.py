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
        exclude = ('template', 'description', )

class ExerciseInDaySerializer(serializers.ModelSerializer):
    exercise_name = serializers.StringRelatedField(source='exercise', read_only=True)
    exercise_id = serializers.IntegerField(source='exercise.id', read_only=True)  
    exercise = serializers.PrimaryKeyRelatedField(queryset=Exercise.objects.all(), write_only=True)
    body_part = serializers.StringRelatedField(source='exercise.body_part', read_only=True)

    class Meta:
        model = ExerciseInDay
        fields = ['id','program_day','exercise','exercise_id', 'exercise_name', 'sets', 'reps', 'body_part']

        
class ProgramDaySerializer(serializers.ModelSerializer):
    exercises = ExerciseInDaySerializer(many=True, source='exerciseinday_set')

    class Meta:
        model = ProgramDay
        fields = ['id', 'workout_program', 'day_of_week', 'day_of_week_integer', 'rest_day', 'exercises']





# Nested Serializers for the retrieving of data

class DaySerializer(serializers.ModelSerializer):
    exercises = ExerciseInDaySerializer(many=True, read_only=True)

    class Meta:
        model = ProgramDay
        fields = ['id', 'day_of_week', 'rest_day', 'exercises']


class ProgramSerializer(serializers.ModelSerializer):
    day_of_week = DaySerializer(many=True, read_only=True)
    
    class Meta:
        model = WorkoutProgram
        fields = ['id', 'name', 'day_of_week']        
