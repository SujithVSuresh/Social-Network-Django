# Generated by Django 3.2.6 on 2021-08-14 10:07

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('social', '0003_userprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='followers',
            field=models.ManyToManyField(blank=True, related_name='followers', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='picture',
            field=models.ImageField(blank=True, default='media/profile.png', upload_to='uploads/profile_pictures'),
        ),
    ]
