from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import WorkoutProgram, ExerciseInDay, ProgramDay
from .serializers import *
import pandas as pd
from io import BytesIO
from django.http import HttpResponse
from datetime import datetime, timedelta





class CreateProgramView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = WorkoutProgramSerializer(data=request.data)
        if serializer.is_valid():
            # Save the program without days
            program = serializer.save()

            # Create ProgramDay instances for each day of the week
            days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
            for day in days_of_week:
                ProgramDay.objects.create(workout_program=program, day_of_week=day,
                                           rest_day=False)

            return Response({"id": program.id, "name": program.name}, status=status.HTTP_201_CREATED)
        else:
            print(serializer.errors)
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
    def post(self, request, program_id, day_of_week):
        try:
            # Get the ProgramDay for the given program_id and day_of_week
            program_day = ProgramDay.objects.get(workout_program_id=program_id, day_of_week=day_of_week)

            # Prepare the data for the serializer
            data = request.data.copy()
            #print(data)
            data['program_day'] = program_day.id
            #print(data)

            # Create a new ExerciseInDay using the serializer
            serializer = ExerciseInDaySerializer(data=data)
            #print(serializer)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except ProgramDay.DoesNotExist:
            return Response({"detail": "ProgramDay not found."}, status=status.HTTP_404_NOT_FOUND)
    
    
class EditExerciseView(APIView):
    def put(self, request, exercise_id):
        try:
            # Get the ExerciseInDay for the given id
            exercise_in_day = ExerciseInDay.objects.get(id=exercise_id)
            print(exercise_in_day)
            # Prepare the data for the serializer
            data = request.data.copy()
            print(data)
            # Update the ExerciseInDay using the serializer
            serializer = ExerciseInDaySerializer(exercise_in_day, data=data)
            print(serializer)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except ExerciseInDay.DoesNotExist:
            return Response({"detail": "ExerciseInDay not found."}, status=status.HTTP_404_NOT_FOUND)
    

class DeleteExerciseView(APIView):
    def delete(self, request, exercise_id):
        try:
            # Get the ExerciseInDay for the given id
            exercise_in_day = ExerciseInDay.objects.get(id=exercise_id)

            # Delete the ExerciseInDay
            exercise_in_day.delete()

            return Response(status=status.HTTP_204_NO_CONTENT)

        except ExerciseInDay.DoesNotExist:
            return Response({"detail": "ExerciseInDay not found."}, status=status.HTTP_404_NOT_FOUND)
    
    
# View for retrieving all data of workout program

class RetrieveProgramDaysView(APIView):
    def get(self, request, program_id):
        try:
            program = WorkoutProgram.objects.get(pk=program_id)
            program_serializer = WorkoutProgramSerializer(program)
            print(program_serializer)
            program_days = ProgramDay.objects.filter(workout_program=program)
            program_days_serializer = ProgramDaySerializer(program_days, many=True)
            response_data = {
                'program_name': program_serializer.data['name'],
                'program_days': program_days_serializer.data
            }
            return Response(response_data)
        except WorkoutProgram.DoesNotExist:
            return Response({"detail": "Workout program not found."}, status=status.HTTP_404_NOT_FOUND)
    

class RetrieveProgramView(APIView):
    def get(self, request, program_id):
        try:
            program = WorkoutProgram.objects.get(pk=program_id)
            serializer = WorkoutProgramSerializer(program)
            return Response(serializer.data)
        except WorkoutProgram.DoesNotExist:
            return Response({"detail": "Workout program not found."}, status=status.HTTP_404_NOT_FOUND)


class RetrieveProgramDayView(APIView):
    def get(self, request, program_id):
        try:
            program = WorkoutProgram.objects.get(pk=program_id)
            serializer = ProgramDaySerializer(program)
            return Response(serializer.data)
        except ProgramDay.DoesNotExist:
            return Response({"detail": "Program day not found."}, status=status.HTTP_404_NOT_FOUND)
        

class ExerciseListView(APIView):
    def get(self, request):
        exercises = Exercise.objects.all()
        serializer = ExerciseSerializer(exercises, many=True)
        return Response(serializer.data)
    

class ProgramView(APIView):
    def get(self, request, program_id):
        program = WorkoutProgram.objects.get(id=program_id)
        serializer = ProgramSerializer(program)
        return Response(serializer.data)
    

class RestDayView(APIView):
    def post(self, request, program_id, day_of_week, *args, **kwaargs):
        try:
            program_day = ProgramDay.objects.get(workout_program=program_id, day_of_week=day_of_week)
        except ProgramDay.DoesNotExist:
            return Response({"error": "ProgramDay object now found"},
                            status=status.HTTP_404_NOT_FOUND)
        program_day.rest_day = True
        program_day.save()

        return Response({"message" : "Rest day set successfully "},
                        status=status.HTTP_200_OK)


class NotRestDayView(APIView):
    def post(self, request, program_id, day_of_week, *args, **kwaargs):
        try:
            program_day = ProgramDay.objects.get(workout_program=program_id, day_of_week=day_of_week)
        except ProgramDay.DoesNotExist:
            return Response({"error": "ProgramDay object now found"},
                            status=status.HTTP_404_NOT_FOUND)
        program_day.rest_day = False
        program_day.save()

        return Response({"message" : "Rest day set successfully "},
                        status=status.HTTP_200_OK)
    

class TemplateProgramView(APIView):
    def get(self, request):
        programs = WorkoutProgram.objects.filter(template=True)
        serializer = ProgramSerializer(programs, many=True)
        return Response(serializer.data)
    


class CreateProgramFromTemplateView(APIView):
    def post(self, request, *args, **kwargs):
        template_id = request.data.get('template_id')
        if not template_id:
            return Response({"error": "Template ID is required"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            template = WorkoutProgram.objects.get(id=template_id, template=True)
        except WorkoutProgram.DoesNotExist:
            return Response({"error": "Template does not exist"}, status=status.HTTP_404_NOT_FOUND)

        # Create a new program based on the template
        program = WorkoutProgram.objects.create(name=template.name, template=False)

        # Copy the ProgramDay and ExerciseInDay instances from the template to the new program
        for day in template.programday_set.all():
            new_day = ProgramDay.objects.create(workout_program=program, day_of_week=day.day_of_week, rest_day=day.rest_day)
            for exercise in day.exerciseinday_set.all():
                ExerciseInDay.objects.create(program_day=new_day, exercise=exercise.exercise, sets=exercise.sets, reps=exercise.reps)

        return Response({"id": program.id, "name": program.name}, status=status.HTTP_201_CREATED)
    


    


class GenerateExcelView(APIView):
        def get(self, request, program_id):
            try:
        
                program = WorkoutProgram.objects.get(pk=program_id)
                program_days = ProgramDay.objects.filter(workout_program=program)

                # Serialize the data
                program_serializer = ProgramSerializer(program)
                program_days_serializer = ProgramDaySerializer(program_days, many=True)

                # Create a new Excel file
                output = BytesIO()
                writer = pd.ExcelWriter(output, engine='xlsxwriter')

                date = datetime.now()

                # For each day in the next 90 days
                for _ in range(90):
                    # Get the program for the current day of the week
                    day_of_week = date.strftime('%A')
                    day = next((day for day in program_days_serializer.data if day['day_of_week'] == day_of_week), None)

                    if day is not None:
                        if day['rest_day']:
                            # If it's a rest day, just write "Rest Day" to the sheet
                            data = {'Rest Day': ['']}
                        else:
                            # Otherwise, create a DataFrame for the day's exercises
                            data = {
                                'Exercise': [exercise['exercise_name'] for exercise in day['exercises']],
                                'Sets': [exercise['sets'] for exercise in day['exercises']],
                                'Reps': [exercise['reps'] for exercise in day['exercises']],
                                'Weight': ['' for exercise in day['exercises']],  # Leave weight blank for the user to fill in
                            }
                        df = pd.DataFrame(data)

                        # Add the DataFrame to the Excel writer
                        df.to_excel(writer, sheet_name=date.strftime('%Y-%m-%d'), index=False)  # Use the date as the sheet name

                    # Move to the next day
                    date += timedelta(days=1)

                # Close the pandas Excel writer
                writer.close()

                # Create a response with the Excel file
                output.seek(0)
                filename = f"{program_serializer.data['name']}.xlsx"
                response = HttpResponse(output.read(), content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
                response['Content-Disposition'] = f'attachment; filename={filename}'

                return response
        
            except WorkoutProgram.DoesNotExist:
                return Response({"detail": "Workout program not found."}, status=status.HTTP_404_NOT_FOUND)



