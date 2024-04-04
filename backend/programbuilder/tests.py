from django.test import TestCase

from .models import BodyPart,Exercise, WorkoutProgram, ProgramDay, ExerciseInDay
from .serializers import ExerciseInDaySerializer,DaySerializer



class ExerciseModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        BodyPart.objects.create(body_part='Chest')
        Exercise.objects.create(exercise='Bench Press', body_part=BodyPart.objects.get(id=1))

    def test_exercise_label(self):
        exercise = Exercise.objects.get(id=1)
        field_label = exercise._meta.get_field('exercise').verbose_name
        self.assertEquals(field_label, 'exercise')

    def test_exercise_max_length(self):
        exercise = Exercise.objects.get(id=1)
        max_length = exercise._meta.get_field('exercise').max_length
        self.assertEquals(max_length, 50)

    def test_object_name_is_exercise(self):
        exercise = Exercise.objects.get(id=1)
        expected_object_name = f'{exercise.exercise}'
        self.assertEquals(expected_object_name, str(exercise))


class ExerciseInDaySerializerTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        BodyPart.objects.create(body_part='Chest')
        Exercise.objects.create(exercise='Bench Press', body_part=BodyPart.objects.get(id=1))
        WorkoutProgram.objects.create(name='Workout 1', template=False, description='Workout 1 description')
        ProgramDay.objects.create(workout_program=WorkoutProgram.objects.get(id=1), day_of_week='Monday', rest_day=False)
        ExerciseInDay.objects.create(program_day=ProgramDay.objects.get(id=1), exercise=Exercise.objects.get(id=1), sets=3, reps=10)

    def test_exercise_in_day_serializer(self):
        exercise_in_day = ExerciseInDay.objects.get(id=1)
        serializer = ExerciseInDaySerializer(exercise_in_day)
        self.assertEqual(serializer.data, {
            'id': 1,
            'program_day': 1,
            'exercise_id': 1,
            'exercise_name': 'Bench Press',
            'sets': 3,
            'reps': 10,
            'body_part': 'Chest'
        })
