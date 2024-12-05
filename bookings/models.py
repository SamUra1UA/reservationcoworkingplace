from django.db import models
from django.contrib.auth.models import User

class CoworkingSpace(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    description = models.TextField()
    price_per_hour = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='images/', blank=True, null=True)

    def __str__(self):
        return self.name


class Seat(models.Model):
    top_position = models.DecimalField(max_digits=5, decimal_places=2)  # or IntegerField
    left_position = models.DecimalField(max_digits=5, decimal_places=2)  # or IntegerFiel
    seat_id = models.CharField(max_length=10, unique=True)  # Відповідає data-seat-id у HTML
    is_occupied = models.BooleanField(default=False)       # Чи зайняте місце
    reserved_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
    coworking_space = models.ForeignKey(CoworkingSpace, on_delete=models.CASCADE)

    def __str__(self):
        return f"Seat {self.seat_id} in {self.coworking_space.name}"


class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    coworking_space = models.ForeignKey(CoworkingSpace, on_delete=models.CASCADE)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    confirmed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username} - {self.coworking_space.name} on {self.date}"

class Review(models.Model):
    coworking_space = models.ForeignKey(CoworkingSpace, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField()
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.coworking_space.name}"
