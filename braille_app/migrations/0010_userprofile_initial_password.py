# Generated by Django 5.0 on 2024-09-13 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('braille_app', '0009_alter_activityhistory_date_log'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='initial_password',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]
