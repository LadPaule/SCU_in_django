# Generated by Django 4.0.4 on 2022-04-28 16:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_sponsorpage_sponsorpagecards'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sponsorpagecards',
            name='child_photo',
        ),
        migrations.RemoveField(
            model_name='sponsorpagecards',
            name='page',
        ),
        migrations.DeleteModel(
            name='SponsorPage',
        ),
        migrations.DeleteModel(
            name='SponsorPageCards',
        ),
    ]
