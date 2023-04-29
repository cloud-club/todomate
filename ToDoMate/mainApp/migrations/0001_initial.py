# Generated by Django 4.1.7 on 2023-04-29 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('content', models.TextField()),
                ('schedule_date', models.DateTimeField()),
                ('remind_date', models.IntegerField()),
                ('isActive', models.BooleanField()),
            ],
        ),
    ]
