# Generated by Django 4.2.5 on 2023-09-24 08:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0006_booking_method_of_payment_booking_status_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='description',
            field=models.TextField(blank=True, max_length=300, null=True),
        ),
        migrations.CreateModel(
            name='UploadedFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='uploads/')),
                ('description', models.TextField(blank=True, max_length=300, null=True)),
                ('status', models.PositiveSmallIntegerField(default=0)),
                ('booking', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='uploaded_files', to='bookings.booking')),
            ],
        ),
        migrations.CreateModel(
            name='FilePage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('copies', models.PositiveSmallIntegerField(default=1)),
                ('color', models.PositiveSmallIntegerField(default=0)),
                ('quality', models.PositiveSmallIntegerField(default=0)),
                ('pages', models.CharField(default='ALL', max_length=100)),
                ('comment', models.TextField(blank=True, max_length=100, null=True)),
                ('file', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pages_to_print', to='bookings.uploadedfile')),
            ],
        ),
    ]