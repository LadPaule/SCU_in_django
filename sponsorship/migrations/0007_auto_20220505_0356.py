# Generated by Django 3.2.13 on 2022-05-05 03:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sponsorship', '0006_aboutpage_side_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sponsorpage',
            name='call_to_action',
        ),
        migrations.AlterField(
            model_name='sponsorpage',
            name='child_DOB',
            field=models.DateField(blank=True, null=True),
        ),
    ]
