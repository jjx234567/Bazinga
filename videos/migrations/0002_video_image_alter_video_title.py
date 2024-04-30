# Generated by Django 5.0.4 on 2024-04-26 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='image',
            field=models.FileField(blank=True, upload_to='video_images/'),
        ),
        migrations.AlterField(
            model_name='video',
            name='title',
            field=models.CharField(max_length=1000),
        ),
    ]