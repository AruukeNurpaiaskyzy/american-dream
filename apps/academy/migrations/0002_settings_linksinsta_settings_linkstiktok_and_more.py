# Generated by Django 5.1.7 on 2025-04-07 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academy', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='settings',
            name='linksinsta',
            field=models.URLField(default=1, verbose_name='инста'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='settings',
            name='linkstiktok',
            field=models.URLField(default=1, verbose_name='тикток'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='settings',
            name='linksyoutube',
            field=models.URLField(default=1, verbose_name='ютуб'),
            preserve_default=False,
        ),
    ]
