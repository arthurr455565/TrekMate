from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from .forms import BookingForm, ReviewForm, TrekBookingForm
from .models import Booking, Review


def trek_booking_create(request):
    """Handle trek booking form submission (AJAX)"""
    if request.method == 'POST':
        form = TrekBookingForm(request.POST)
        if form.is_valid():
            try:
                booking = form.save(commit=False, user=request.user if request.user.is_authenticated else None)
                booking.save()
                return JsonResponse({
                    'success': True,
                    'message': 'Booking request submitted successfully! We will contact you soon.'
                })
            except Exception as e:
                return JsonResponse({
                    'success': False,
                    'errors': {'general': [str(e)]}
                }, status=500)
        else:
            return JsonResponse({
                'success': False,
                'errors': form.errors
            }, status=400)
    
    # GET request - return form with pre-filled data if user is logged in
    initial_data = {}
    if request.user.is_authenticated:
        initial_data = {
            'name': request.user.get_full_name() or request.user.username,
            'email': request.user.email
        }
    
    form = TrekBookingForm(initial=initial_data)
    return render(request, 'bookings/trek_booking_form.html', {'form': form})


@login_required
def booking_create(request):
    if request.user.role != 'trekker':
        return redirect('trek_list')

    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.trekker = request.user
            booking.save()
            return redirect('booking_list')
    else:
        form = BookingForm()
    return render(request, 'bookings/booking_form.html', {'form': form})


@login_required
def booking_list(request):
    if request.user.role == 'trekker':
        bookings = Booking.objects.filter(trekker=request.user)
    elif request.user.role == 'guide':
        bookings = Booking.objects.filter(guide__user=request.user)
    else:
        bookings = Booking.objects.all()
    return render(request, 'bookings/booking_list.html', {'bookings': bookings})


@login_required
def add_review(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)

    if booking.trekker != request.user:
        return redirect('booking_list')

    try:
        review = booking.review
        return redirect('booking_list')
    except Review.DoesNotExist:
        pass

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.booking = booking
            review.save()
            return redirect('booking_list')
    else:
        form = ReviewForm()

    return render(request, 'bookings/review_form.html', {'form': form, 'booking': booking})
