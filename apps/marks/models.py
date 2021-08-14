from django.db import models
from django.db.models import CASCADE

import apps.assignments.models
import apps.students.models
import apps.classes.models


class Marks(models.Model):
    class Meta:
        db_table = 'marks'
        unique_together = ['assignment_id', 'student_id']  # Compund primary key

    assignment_id = models.OneToOneField(apps.assignments.models.Assignment, on_delete=CASCADE)
    class_id = models.OneToOneField(apps.classes.models.Classes, on_delete=CASCADE)
    student_id = models.OneToOneField(apps.students.models.Student, on_delete=CASCADE)
    mark_awarded = models.DecimalField(max_digits=3, decimal_places=1)


