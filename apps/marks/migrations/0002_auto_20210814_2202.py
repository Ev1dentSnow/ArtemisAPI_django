# Generated by Django 3.2.5 on 2021-08-14 20:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('marks', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='marks',
            old_name='assignment_id',
            new_name='assignment',
        ),
        migrations.RenameField(
            model_name='marks',
            old_name='student_id',
            new_name='student',
        ),
    ]
