# Generated by Django 5.2.1 on 2025-06-04 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0002_rename_subjec_teacher_subject'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='email',
            field=models.EmailField(max_length=20),
        ),
    ]
