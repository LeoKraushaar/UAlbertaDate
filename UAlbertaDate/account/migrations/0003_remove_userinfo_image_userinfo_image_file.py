# Generated by Django 4.1.3 on 2022-11-06 02:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_userinfo_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userinfo',
            name='image',
        ),
        migrations.AddField(
            model_name='userinfo',
            name='image_file',
            field=models.ImageField(blank=True, null=True, upload_to='images/%Y/%m/%d'),
        ),
    ]
