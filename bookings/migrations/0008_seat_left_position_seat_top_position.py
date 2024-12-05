# Generated by Django 5.1.3 on 2024-11-15 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0007_remove_coworkingspace_seating_map_remove_seat_x_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='seat',
            name='left_position',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='seat',
            name='top_position',
            field=models.DecimalField(decimal_places=2, default=7, max_digits=5),
            preserve_default=False,
        ),
    ]