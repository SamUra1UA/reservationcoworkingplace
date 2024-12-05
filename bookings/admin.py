from django.contrib import admin
from .models import CoworkingSpace, Booking, Review, Seat

# Налаштування для відображення моделі CoworkingSpace в адмін-панелі
@admin.register(CoworkingSpace)
class CoworkingSpaceAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'price_per_hour')
    search_fields = ('name', 'address')
    list_filter = ('price_per_hour',)

# Налаштування для відображення моделі Booking в адмін-панелі
@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('coworking_space', 'user', 'date', 'start_time', 'end_time', 'confirmed')
    search_fields = ('coworking_space__name', 'user__username')
    list_filter = ('date', 'start_time', 'end_time', 'confirmed')

# Налаштування для відображення моделі Review в адмін-панелі
@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('coworking_space', 'user', 'rating', 'created_at')
    search_fields = ('coworking_space__name', 'user__username')
    list_filter = ('rating', 'created_at')

# Налаштування для відображення моделі Seat в адмін-панелі
@admin.register(Seat)
class SeatAdmin(admin.ModelAdmin):
    list_display = ('seat_id', 'get_coworking_space', 'reserved_by', 'is_occupied')
    search_fields = ('coworking_space__name', 'reserved_by__username', 'seat_id')  # Додав seat_id до пошуку
    list_filter = ('is_occupied',)

    def get_coworking_space(self, seat):
        return seat.coworking_space.name if seat.coworking_space else 'No coworking space'
    get_coworking_space.short_description = 'Coworking Space'
