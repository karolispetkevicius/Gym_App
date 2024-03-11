from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import WorkoutProgram, ExerciseInDay, ProgramDay
from .serializers import *




class CreateProgramView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = WorkoutProgramSerializer(data=request.data)
        if serializer.is_valid():
            # Save the program without days
            program = serializer.save()
            return Response({"id": program.id, "name": program.name}, status=status.HTTP_201_CREATED)
        else:
            print (serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class UpdateProgramView(APIView):
    def put(self, request, program_id, *args, **kwargs):
        program = WorkoutProgram.objects.get(pk=program_id)
        serializer = WorkoutProgramSerializer(program, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class DeleteProgramView(APIView):
    def delete(self, request, program_id, *args, **kwargs):
        program = WorkoutProgram.objects.get(pk=program_id)
        program.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



class AddDayView(APIView):
    def post(self, request, program_id, *args, **kwargs):
        # Retrieve the workout program
        try:
            workout_program = WorkoutProgram.objects.get(pk=program_id)
        except WorkoutProgram.DoesNotExist:
            return Response({"detail": "Workout program not found."}, status=status.HTTP_404_NOT_FOUND)
        
        # Validate and save the new day
        serializer = ProgramDaySerializer(data=request.data)
        if serializer.is_valid():
            # Save the program day
            program_day = serializer.save(workout_program=workout_program)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            print(serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class UpdateDayView(APIView):
    def put(self, request, program_id, day_id, *args, **kwargs):
        # Retrieve the workout program
        try:
            workout_program = WorkoutProgram.objects.get(pk=program_id)
        except WorkoutProgram.DoesNotExist:
            return Response({"detail": "Workout program not found."}, status=status.HTTP_404_NOT_FOUND)
        
        # Retrieve the day
        try:
            program_day = ProgramDay.objects.get(pk=day_id)
        except ProgramDay.DoesNotExist:
            return Response({"detail": "Day not found."}, status=status.HTTP_404_NOT_FOUND)
        
        # Validate and update the day
        serializer = ProgramDaySerializer(program_day, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class DeleteDayView(APIView):
    def delete(self, request, program_id, day_id, *args, **kwargs):
        # Retrieve the workout program
        try:
            workout_program = WorkoutProgram.objects.get(pk=program_id)
        except WorkoutProgram.DoesNotExist:
            return Response({"detail": "Workout program not found."}, status=status.HTTP_404_NOT_FOUND)
        
        # Retrieve the day
        try:
            program_day = ProgramDay.objects.get(pk=day_id)
        except ProgramDay.DoesNotExist:
            return Response({"detail": "Day not found."}, status=status.HTTP_404_NOT_FOUND)
        
        # Delete the day
        program_day.delete()


class AddExerciseView(APIView):
    def post(self, request, day_id, *args, **kwargs):
        try:
        # Retrieve program day based on program ID and order
            program_day = ProgramDay.objects.get(pk=day_id)
        except ProgramDay.DoesNotExist:
            return Response({"detail": "Program day not found."}, status=status.HTTP_404_NOT_FOUND)
        
        # Validate and save the new exercise
        serializer = ExerciseInDaySerializer(data=request.data)
        if serializer.is_valid():
            # Save the exercise
            exercise_in_day = serializer.save(program_day=program_day)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            print(serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
class UpdateExerciseView(APIView):
    def put(self, request, program_id, exercise_id, *args, **kwargs):
        # Retrieve the exercise in day instance to update
        try:
            exercise_in_day = ExerciseInDay.objects.get(program_day__program_id=program_id, exercise_id=exercise_id)
        except ExerciseInDay.DoesNotExist:
            return Response({"detail": "Exercise in day not found."}, status=status.HTTP_404_NOT_FOUND)
        
        # Update the exercise details
        serializer = ExerciseInDaySerializer(exercise_in_day, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class DeleteExerciseView(APIView):
    def delete(self, request, program_id, exercise_id, *args, **kwargs):
        # Retrieve the exercise in day instance to delete
        try:
            exercise_in_day = ExerciseInDay.objects.get(program_day__program_id=program_id, exercise_id=exercise_id)
        except ExerciseInDay.DoesNotExist:
            return Response({"detail": "Exercise in day not found."}, status=status.HTTP_404_NOT_FOUND)
        
        # Delete the exercise in day instance
        exercise_in_day.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    

class RetrieveProgramView(APIView):
    def get(self, request, program_id):
        try:
            program = WorkoutProgram.objects.get(pk=program_id)
            serializer = WorkoutProgramSerializer(program)
            return Response(serializer.data)
        except WorkoutProgram.DoesNotExist:
            return Response({"detail": "Workout program not found."}, status=status.HTTP_404_NOT_FOUND)
        

class ListProgramDaysView(APIView):
    def get(self, request, program_id):
        try:
            program_days = ProgramDay.objects.filter(pk=program_id)
            serializer = ProgramDaySerializer(program_days, many=True)
            return Response(serializer.data)
        except ProgramDay.DoesNotExist:
            return Response({"detail": "Program days not found."}, status=status.HTTP_404_NOT_FOUND)
    

class RetrieveProgramDayView(APIView):
    def get(self, request, program_day_id):
        try:
            program_day = ProgramDay.objects.get(pk=program_day_id)
            serializer = ProgramDaySerializer(program_day)
            return Response(serializer.data)
        except ProgramDay.DoesNotExist:
            return Response({"detail": "Program day not found."}, status=status.HTTP_404_NOT_FOUND)
        

class ExerciseListView(APIView):
    def get(self, request):
        exercises = Exercise.objects.all()
        serializer = ExerciseSerializer(exercises, many=True)
        return Response(serializer.data)