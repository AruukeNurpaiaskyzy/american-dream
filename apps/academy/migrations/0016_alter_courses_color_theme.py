# Generated by Django 5.1.7 on 2025-04-04 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academy', '0015_courses_coursesprogram_delete_course'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courses',
            name='color_theme',
            field=models.CharField(help_text='Цвет темы: light-purple, dark-blue, green и т.д.', max_length=50),
        ),
    ]
