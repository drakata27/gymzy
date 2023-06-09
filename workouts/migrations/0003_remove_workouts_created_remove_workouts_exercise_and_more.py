# Generated by Django 4.2 on 2023-05-11 13:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('workouts', '0002_workouts_sets_alter_workouts_weight'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='workouts',
            name='created',
        ),
        migrations.RemoveField(
            model_name='workouts',
            name='exercise',
        ),
        migrations.RemoveField(
            model_name='workouts',
            name='reps',
        ),
        migrations.RemoveField(
            model_name='workouts',
            name='sets',
        ),
        migrations.RemoveField(
            model_name='workouts',
            name='weight',
        ),
        migrations.CreateModel(
            name='Exercise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exercise', models.CharField(max_length=100)),
                ('weight', models.DecimalField(decimal_places=2, max_digits=5)),
                ('reps', models.IntegerField()),
                ('sets', models.IntegerField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('workouts', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='workouts.workouts')),
            ],
        ),
    ]
