# Generated by Django 3.0.5 on 2023-07-05 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0006_question_audio'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='qtype',
            field=models.CharField(blank=True, choices=[('Fill in the blanks', 'Fill in the blanks'), ('MCQ', 'MCQ')], max_length=100, null=True),
        ),
    ]
