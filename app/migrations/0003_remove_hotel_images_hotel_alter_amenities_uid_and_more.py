# Generated by Django 5.0.1 on 2024-01-10 06:34

import django.db.models.deletion
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_amenities_uid_alter_hotel_uid_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hotel_images',
            name='hotel',
        ),
        migrations.AlterField(
            model_name='amenities',
            name='uid',
            field=models.UUIDField(default=uuid.UUID('f4b3cf73-ef9a-4c68-abef-6d062cae70fa'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='hotel',
            name='uid',
            field=models.UUIDField(default=uuid.UUID('f4b3cf73-ef9a-4c68-abef-6d062cae70fa'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.CreateModel(
            name='HotelBooking',
            fields=[
                ('uid', models.UUIDField(default=uuid.UUID('f4b3cf73-ef9a-4c68-abef-6d062cae70fa'), editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now_add=True)),
                ('start_at', models.DateField()),
                ('end_at', models.DateField()),
                ('booking_type', models.CharField(choices=[('Pre Book', 'Pre Book'), ('Post Book', 'Post Book')], max_length=180)),
                ('hotel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hotel_booking', to='app.hotel')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_booking', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='HotelImages',
            fields=[
                ('uid', models.UUIDField(default=uuid.UUID('f4b3cf73-ef9a-4c68-abef-6d062cae70fa'), editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now_add=True)),
                ('images', models.ImageField(upload_to='hotel/')),
                ('hotel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='app.hotel')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.DeleteModel(
            name='Hotel_Booking',
        ),
        migrations.DeleteModel(
            name='Hotel_Images',
        ),
    ]
