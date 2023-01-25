# Generated by Django 4.1.5 on 2023-01-23 13:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Film',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('description', models.CharField(max_length=120)),
                ('length', models.IntegerField()),
                ('category', models.CharField(choices=[('ACTION', 'Action'), ('COMEDY', 'Comedy'), ('KIDS', 'For kids'), ('THRILLER', 'Thriller'), ('ROMANCE', 'Romance'), ('CRIME', 'Crime'), ('SCIFI', 'Sci-Fi'), ('MUSICAL', 'Musical')], default=None, max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Hall',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('capacity', models.IntegerField()),
                ('description', models.CharField(max_length=120)),
                ('max_row', models.CharField(max_length=3)),
                ('max_col', models.CharField(max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='Seat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seat_category', models.CharField(choices=[('NORMAL', 'Normal'), ('COMFORT', 'Comfort'), ('VIP', 'Vip')], default='NORMAL', max_length=12)),
                ('place', models.CharField(max_length=3)),
                ('description', models.CharField(max_length=120, null=True)),
                ('hall_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='theatre.hall')),
            ],
        ),
    ]