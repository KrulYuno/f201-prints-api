# Generated by Django 4.2.5 on 2023-09-27 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0007_booking_description_uploadedfile_filepage'),
    ]

    operations = [
        migrations.RenameField(
            model_name='filepage',
            old_name='copies',
            new_name='quantity',
        ),
        migrations.AddField(
            model_name='filepage',
            name='paper_type',
            field=models.CharField(blank=True, max_length=16, null=True),
        ),
    ]
