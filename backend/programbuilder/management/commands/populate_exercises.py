from django.core.management.base import BaseCommand
from programbuilder.models import Exercise, BodyPart

class Command(BaseCommand):
    help = 'Populate exercises in the database'

    def handle(self, *args, **options):
        exercises_by_body_part = {
             
        'Chest': [
            'Bar Dip', 'Bench Press', 'Cable Chest Press', 'Close-Grip Bench Press',
            'Close-Grip Feet-Up Bench Press', 'Decline Bench Press', 'Dumbbell Chest Fly',
            'Dumbbell Chest Press', 'Dumbbell Decline Chest Press', 'Dumbbell Floor Press',
            'Dumbbell Pullover', 'Feet-Up Bench Press', 'Floor Press', 'Incline Bench Press',
            'Incline Dumbbell Press', 'Incline Push-Up', 'Kettlebell Floor Press',
            'Kneeling Incline Push-Up', 'Kneeling Push-Up', 'Machine Chest Fly',
            'Machine Chest Press', 'Pec Deck', 'Push-Up', 'Push-Up Against Wall',
            'Push-Ups With Feet in Rings', 'Resistance Band Chest Fly', 'Smith Machine Bench Press',
            'Smith Machine Incline Bench Press', 'Standing Cable Chest Fly', 'Standing Resistance Band Chest Fly'
        ],

        'Shoulders': [
            'Band External Shoulder Rotation', 'Band Internal Shoulder Rotation', 'Band Pull-Apart',
            'Barbell Front Raise', 'Barbell Rear Delt Row', 'Barbell Upright Row', 'Behind the Neck Press',
            'Cable Lateral Raise', 'Cable Rear Delt Row', 'Dumbbell Front Raise', 'Dumbbell Horizontal Internal Shoulder Rotation',
            'Dumbbell Horizontal External Shoulder Rotation', 'Dumbbell Lateral Raise', 'Dumbbell Rear Delt Row',
            'Dumbbell Shoulder Press', 'Face Pull', 'Front Hold', 'Lying Dumbbell External Shoulder Rotation',
            'Lying Dumbbell Internal Shoulder Rotation', 'Machine Lateral Raise', 'Machine Shoulder Press',
            'Monkey Row', 'Overhead Press', 'Plate Front Raise', 'Power Jerk', 'Push Press',
            'Reverse Cable Flyes', 'Reverse Dumbbell Flyes', 'Reverse Machine Fly', 'Seated Dumbbell Shoulder Press',
            'Seated Barbell Overhead Press', 'Seated Smith Machine Shoulder Press', 'Snatch Grip Behind the Neck Press',
            'Squat Jerk', 'Split Jerk'
        ],

        'Biceps': [
            'Barbell Curl', 'Barbell Preacher Curl', 'Bodyweight Curl', 'Cable Curl With Bar',
            'Cable Curl With Rope', 'Concentration Curl', 'Dumbbell Curl', 'Dumbbell Preacher Curl', 'Hammer Curl',
            'Incline Dumbbell Curl', 'Machine Bicep Curl', 'Spider Curl'
        ],

        'Triceps': [
            'Barbell Standing Triceps Extension', 'Barbell Lying Triceps Extension', 'Bench Dip', 'Close-Grip Push-Up',
            'Dumbbell Lying Triceps Extension', 'Dumbbell Standing Triceps Extension', 'Overhead Cable Triceps Extension',
            'Tricep Bodyweight Extension', 'Tricep Pushdown With Bar', 'Tricep Pushdown With Rope'
        ],

        'Legs': [
            'Air Squat', 'Barbell Hack Squat', 'Barbell Lunge', 'Barbell Walking Lunge',
            'Belt Squat', 'Body Weight Lunge', 'Bodyweight Leg Curl', 'Box Squat', 'Bulgarian Split Squat', 'Chair Squat',
            'Dumbbell Lunge', 'Dumbbell Squat', 'Front Squat', 'Goblet Squat', 'Hack Squat Machine', 'Half Air Squat',
            'Hip Adduction Machine', 'Jumping Lunge', 'Landmine Hack Squat', 'Landmine Squat', 'Leg Curl On Ball',
            'Leg Extension', 'Leg Press', 'Lying Leg Curl', 'Pause Squat', 'Romanian Deadlift', 'Safety Bar Squat',
            'Seated Leg Curl', 'Shallow Body Weight Lunge', 'Side Lunges (Bodyweight)', 'Smith Machine Squat', 'Squat', 'Step Up'
        ],

        'Back': [
            'Assisted Chin-Up', 'Assisted Pull-Up', 'Back Extension', 'Barbell Row', 'Barbell Shrug', 'Block Clean',
            'Block Snatch', 'Cable Close Grip Seated Row', 'Cable Wide Grip Seated Row', 'Chin-Up', 'Clean', 'Clean and Jerk',
            'Deadlift', 'Deficit Deadlift', 'Dumbbell Deadlift', 'Dumbbell Row', 'Dumbbell Shrug', 'Floor Back Extension',
            'Good Morning', 'Hang Clean', 'Hang Power Clean', 'Hang Power Snatch', 'Hang Snatch', 'Inverted Row',
            'Inverted Row with Underhand Grip', 'Jefferson Curl', 'Kettlebell Swing', 'Lat Pulldown With Pronated Grip',
            'Lat Pulldown With Supinated Grip', 'One-Handed Cable Row', 'One-Handed Lat Pulldown', 'Pause Deadlift',
            'Pendlay Row', 'Power Clean', 'Power Snatch', 'Pull-Up', 'Pull-Up With a Neutral Grip', 'Rack Pull', 'Seal Row',
            'Seated Machine Row', 'Snatch', 'Snatch Grip Deadlift', 'Stiff-Legged Deadlift', 'Straight Arm Lat Pulldown',
            'Sumo Deadlift', 'T-Bar Row', 'Trap Bar Deadlift With High Handles', 'Trap Bar Deadlift With Low Handles'
        ],

        'Glutes': [
            'Banded Side Kicks', 'Cable Pull Through', 'Clamshells', 'Dumbbell Romanian Deadlift', 'Dumbbell Frog Pumps',
            'Fire Hydrants', 'Frog Pumps', 'Glute Bridge', 'Hip Abduction Against Band', 'Hip Abduction Machine', 'Hip Thrust',
            'Hip Thrust Machine', 'Hip Thrust With Band Around Knees', 'Lateral Walk With Band', 'Machine Glute Kickbacks',
            'One-Legged Glute Bridge', 'One-Legged Hip Thrust', 'Romanian Deadlift', 'Single Leg Romanian Deadlift',
            'Standing Glute Kickback in Machine', 'Step Up'
        ],

        'Abs': [
            'Ball Slams', 'Cable Crunch', 'Crunch', 'Dead Bug', 'Hanging Leg Raise', 'Hanging Knee Raise', 'Hanging Sit-Up',
            'High to Low Wood Chop with Band', 'Horizontal Wood Chop with Band', 'Kneeling Ab Wheel Roll-Out', 'Kneeling Plank',
            'Kneeling Side Plank', 'Lying Leg Raise', 'Lying Windshield Wiper', 'Lying Windshield Wiper with Bent Knees',
            'Machine Crunch', 'Mountain Climbers', 'Oblique Crunch', 'Oblique Sit-Up', 'Plank', 'Plank with Leg Lifts', 'Side Plank',
            'Sit-Up'
        ],
        
        'Calves': [
            'Eccentric Heel Drop', 'Heel Raise', 'Seated Calf Raise', 'Standing Calf Raise'
        ]
        }

        for body_part_name, exercises_list in exercises_by_body_part.items():
                body_part, _ = BodyPart.objects.get_or_create(body_part=body_part_name)
                for exercise in exercises_list:
                    Exercise.objects.get_or_create(exercise=exercise, body_part=body_part)

        self.stdout.write(self.style.SUCCESS('Exercises successfully populated'))