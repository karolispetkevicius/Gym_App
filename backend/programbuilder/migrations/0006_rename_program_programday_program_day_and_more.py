# Generated by Django 5.0.2 on 2024-03-05 20:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('programbuilder', '0005_alter_programday_rest_day'),
    ]

    operations = [
        migrations.RenameField(
            model_name='programday',
            old_name='program',
            new_name='program_day',
        ),
        migrations.AlterUniqueTogether(
            name='programday',
            unique_together={('program_day', 'order')},
        ),
    ]
