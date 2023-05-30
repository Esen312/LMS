# Generated by Django 4.2 on 2023-05-29 10:29

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, unique=True, verbose_name='Название')),
                ('content', models.TextField(verbose_name='Описание')),
                ('price', models.IntegerField(verbose_name='Цена курса: ')),
                ('price_before_discount', models.IntegerField(default=100000)),
                ('discount', models.IntegerField(default=10, verbose_name='Скидка: ')),
                ('discount_confirmation', models.BooleanField(default=False, verbose_name='Начать акцию')),
                ('start_day', models.DateField(default=datetime.date(2023, 5, 29), verbose_name='День старта скидок: ')),
                ('end_day', models.DateField(default=datetime.date(2023, 5, 30), verbose_name='День окончания скидок: ')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lms.category')),
            ],
        ),
        migrations.CreateModel(
            name='UserCourse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lms.course')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('preview', models.FileField(upload_to='media/')),
                ('content', models.TextField()),
                ('course_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lms.course')),
            ],
        ),
    ]