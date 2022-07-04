# Generated by Django 3.2.4 on 2022-05-23 13:38

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('floatapp', '0002_screenshot_blurhash'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='screenshot',
            options={'ordering': ['id']},
        ),
        migrations.AddField(
            model_name='userdetail',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userdetail',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
