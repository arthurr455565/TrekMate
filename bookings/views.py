from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import BookingForm
from .models import Booking
from .models import Review
from .forms import ReviewForm

@login_required
def booking_create(request):
    if request.user.role != 'trekker':
        return redirect('trek_list')  # only trekkers can book

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
        bookings = Booking.objects.all()  # admin
    return render(request, 'bookings/booking_list.html', {'bookings': bookings})



@login_required
def add_review(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)

    # Only the trekker who made the booking can review
    if booking.trekker != request.user:
        return redirect('booking_list')

    # Check if review already exists
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
