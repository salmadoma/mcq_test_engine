# Generated by Django 4.1.2 on 2022-10-08 03:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mcq_test_app', '0002_student_delete_quiz_student_phone_unique_constraint'),
    ]

    operations = [
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Topic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mcq_test_app.topic')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mcq_test_app.student')),
            ],
        ),
    ]
