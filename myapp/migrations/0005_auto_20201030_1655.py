# Generated by Django 3.0.7 on 2020-10-30 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_auto_20201030_1244'),
    ]

    operations = [
        migrations.RenameField(
            model_name='trainer',
            old_name='image',
            new_name='trainer_image',
        ),
        migrations.AddField(
            model_name='course',
            name='courses_image',
            field=models.ImageField(default='', upload_to='img/courses'),
        ),
    ]
