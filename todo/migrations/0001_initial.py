# Generated by Django 2.0.13 on 2019-06-04 23:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Имя проекта', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Tasks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Имя задачи', max_length=100)),
                ('priority', models.IntegerField(default=2)),
                ('todo_date', models.DateTimeField(auto_now=True)),
                ('task_status', models.BooleanField(default=False)),
            ],
        ),
    ]
