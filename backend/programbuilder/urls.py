from django.urls import path, include
from django.contrib import admin
from .views import *
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)












urlpatterns = [
    path('programs/create/', CreateProgramView.as_view(), name='create_program'),


    path('programs/<int:program_id>/add_day/', AddDayView.as_view(), name='add_day'),
    path('programs/<int:program_id>/days/<int:day_id>/update/', UpdateDayView.as_view(), name='update_day'),
    path('programs/<int:program_id>/days/<int:day_id>/delete/', DeleteDayView.as_view(), name='delete_day'),


    path('programs/<int:program_id>/days/<str:day_of_week>/exercises/add/',AddExerciseView.as_view(), name='add_exercise'), 
    path('exercises/<int:exercise_id>/edit/', EditExerciseView.as_view(), name='edit_exercise'),
    path('exercises/<int:exercise_id>/delete/', DeleteExerciseView.as_view(), name='delete_exercise'),
    
    path('programs/<int:program_id>/', RetrieveProgramView.as_view(), name='retrieve_program'),
    path('programs/<int:program_id>/days/', RetrieveProgramDaysView.as_view(), name='list_program_days'),
    path('programs/days/<int:program_day_id>/', RetrieveProgramDayView.as_view(), name='retrieve_program_day'),

    path('exercises/', ExerciseListView.as_view(), name='exercises'),

    path('programs/<int:program_id>/days/<str:day_of_week>/rest', RestDayView.as_view(), name='rest_day'),
    path('programs/<int:program_id>/days/<str:day_of_week>/notrest', NotRestDayView.as_view(), name='not_rest_day'),

    path('programs/templates/', TemplateProgramView.as_view(), name='template_programs'),
    path('programs/create_from_template', CreateProgramFromTemplateView.as_view(), name='program_from_template'),

    path('programbuilder/generate/<int:program_id>/', GenerateExcelView.as_view(), name='generate_excel'),

    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),


]