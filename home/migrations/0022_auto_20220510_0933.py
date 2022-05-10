# Generated by Django 3.2.13 on 2022-05-10 09:33

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0023_add_choose_permissions'),
        ('home', '0021_auto_20220509_1847'),
    ]

    operations = [
        migrations.AddField(
            model_name='childsponsorshippage',
            name='design_image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image'),
        ),
        migrations.CreateModel(
            name='Childsponsoshipfaqs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('question', models.CharField(blank=True, max_length=500, null=True)),
                ('answer', models.CharField(blank=True, max_length=500, null=True)),
                ('page', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='faqs', to='home.childsponsorshippage')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
    ]