# Generated by Django 4.1.3 on 2022-11-06 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0008_remove_userinfo_liked_users'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='first_name',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
    ]
