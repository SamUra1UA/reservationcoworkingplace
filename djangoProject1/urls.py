from django.contrib import admin
from django.urls import path, include
from bookings import views as booking_views
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings
from bookings.forms import BookingForm

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', booking_views.register, name='register'),
    path('login/', include('django.contrib.auth.urls')),  # логін/логаут
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('', booking_views.coworking_space_list, name='coworking_space_list'),
    path('space/<int:space_id>/', booking_views.coworking_space_detail, name='coworking_space_detail'),
    path('get_seats/<int:coworking_space_id>/', booking_views.get_seats, name='get_seats'),
    path('reserve_seat/<int:seat_id>/', booking_views.reserve_seat, name='reserve_seat'),
    path('space/<int:space_id>/add_review/', booking_views.add_review, name='add_review'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
