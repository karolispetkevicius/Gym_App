from django.urls import path, include
from django.contrib import admin
from .views import *

urlpatterns = [
    path('programs/create/', CreateProgramView.as_view(), name='create_program'),
    path('programs/<int:program_id>/update/', UpdateProgramView.as_view(), name='update_program'),
    path('programs/<int:program_id>/delete/', DeleteProgramView.as_view(), name='delete_program'),

    path('programs/<int:program_id>/add_day/', AddDayView.as_view(), name='add_day'),
    path('programs/<int:program_id>/days/<int:day_id>/update/', UpdateDayView.as_view(), name='update_day'),
    path('programs/<int:program_id>/days/<int:day_id>/delete/', DeleteDayView.as_view(), name='delete_day'),


    path('days/<int:day_id>/add_exercise/', AddExerciseView.as_view(), name='add_exercise'),
    path('programs/<int:program_id>/exercises/<int:exercise_id>/update/', UpdateExerciseView.as_view(), name='update_exercise'),
    path('programs/<int:program_id>/exercises/<int:exercise_id>/delete/', DeleteExerciseView.as_view(), name='delete_exercise'),
    
    path('programs/<int:program_id>/', RetrieveProgramView.as_view(), name='retrieve_program'),
    path('programs/<int:program_id>/days/', ListProgramDaysView.as_view(), name='list_program_days'),
    path('programs/days/<int:program_day_id>/', RetrieveProgramDayView.as_view(), name='retrieve_program_day'),

    path('exercises/', ExerciseListView.as_view(), name='exercises'),
    path('programs/<int:program_id/', RetrieveProgramView.as_view(), name='program')
]