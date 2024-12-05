from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegisterForm
from .models import CoworkingSpace, Seat, Review
from .forms import ReviewForm
import requests

def coworking_space_list(request):
    spaces = CoworkingSpace.objects.all()
    return render(request, 'coworking_space_list.html', {'spaces': spaces})

@login_required
def coworking_space_detail(request, space_id):
    coworking_space = get_object_or_404(CoworkingSpace, id=space_id)
    reviews = Review.objects.filter(coworking_space=coworking_space)
    return render(request, 'coworking_space_detail.html', {
        'coworking_space': coworking_space,
        'reviews': reviews
    })

def get_seats(request, coworking_space_id):
    seats = Seat.objects.filter(coworking_space_id=coworking_space_id)
    seats_data = [
        {
            'seat_id': seat.id,
            'is_occupied': seat.is_occupied,
            'top_position': seat.top_position,
            'left_position': seat.left_position
        }
        for seat in seats
    ]
    return JsonResponse({'seats': seats_data})

@csrf_exempt
@login_required
def reserve_seat(request, seat_id):
    if request.method == 'POST':
        try:
            seat = Seat.objects.get(id=seat_id)
            if seat.is_occupied:
                return JsonResponse({'success': False, 'error': 'Seat is already occupied.'})

            seat.is_occupied = True
            seat.reserved_by = request.user
            seat.save()

            return JsonResponse({'success': True, 'message': f'Seat {seat_id} reserved successfully!'})
        except Seat.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Seat does not exist.'})

    return JsonResponse({'success': False, 'error': 'Invalid request method.'})

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Акаунт для {username} створено! Тепер ви можете увійти.')
            return redirect('login')
        else:
            messages.error(request, 'Будь ласка, виправте помилки у формі.')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})

@login_required
def add_review(request, space_id):
    coworking_space = get_object_or_404(CoworkingSpace, id=space_id)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.coworking_space = coworking_space
            review.save()
            return JsonResponse({'success': True, 'message': 'Review added successfully!'})
        else:
            return JsonResponse({'success': False, 'errors': form.errors})

    return JsonResponse({'success': False, 'error': 'Invalid request method.'})