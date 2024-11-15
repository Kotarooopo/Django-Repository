# Generated by Django 5.0.4 on 2024-07-31 05:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='score',
            name='initial_grade',
        ),
        migrations.AlterField(
            model_name='class',
            name='teacher',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.teacher'),
        ),
        migrations.DeleteModel(
            name='TotalInitialGrade',
        ),
    ]
