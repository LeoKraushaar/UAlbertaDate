# Generated by Django 4.1.3 on 2022-11-06 02:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_remove_userinfo_image_userinfo_image_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='image_file',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
