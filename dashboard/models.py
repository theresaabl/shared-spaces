from django.db import models
from django.core.exceptions import ValidationError
from datetime import datetime, timedelta
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class EventSpace(models.Model):
    name = models.CharField(max_length=200, unique=True)
    type = models.CharField(max_length=200)
    image = CloudinaryField('image', default='placeholder')
    building = models.CharField(max_length=200)
    capacity = models.PositiveSmallIntegerField()
    number_of_tables = models.PositiveSmallIntegerField()
    number_of_chairs = models.PositiveSmallIntegerField()
    kitchen = models.BooleanField()
    tea_and_coffeemaker = models.BooleanField()
    projector = models.BooleanField()
    audio_equipment = models.BooleanField()
    childrens_play_area = models.BooleanField()
    piano = models.BooleanField()
    notes = models.TextField(blank=True)

    def __str__(self):
        return self.name


class EventSpaceBooking(models.Model):
    """
    Code inspiration to display integer choices labels:
    https://medium.com/@alex.kirkup/integerchoices-in-django-models-working-seamlessly-from-the-backend-and-the-frontend-using-labels-a3e77b86d419  # noqa
    """

    class Status(models.IntegerChoices):
        PENDING = 0, "Pending"
        APPROVED = 1, "Approved"
        DENIED = 2, "Denied"

    resident = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="event_space_bookings_by_user"
        )
    event_space = models.ForeignKey(
        EventSpace,
        on_delete=models.CASCADE,
        related_name="event_space_bookings_by_space"
        )
    occasion = models.CharField(max_length=200)
    date = models.DateField()
    start = models.TimeField()
    end = models.TimeField()
    notes = models.TextField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(
        choices=Status.choices,
        default=Status.PENDING
        )

    def clean(self):
        """Ensure start_time is before end_time and at least 1 hour apart."""
        if self.start >= self.end:
            raise ValidationError("End time must be later than start time.")

        # Convert to datetime for proper time difference calculation
        start_dt = datetime.combine(datetime.today(), self.start)
        end_dt = datetime.combine(datetime.today(), self.end)

        if end_dt - start_dt < timedelta(hours=1):
            raise ValidationError("End time must be at least 1 hour after start time.")

        duplicate_bookings = EventSpaceBooking.objects.filter(
                            event_space=self.event_space,
                            date=self.date
                            ).exclude(id=self.id)
        
        for booking in duplicate_bookings:
            # convert booking start and end time to datetime objects 
            # and substract/add 1 hour to get a window between bookings
            booking_start_dt = datetime.combine(datetime.today(), booking.start) - timedelta(hours=1)
            booking_end_dt = datetime.combine(datetime.today(), booking.end) + timedelta(hours=1)
            if start_dt < booking_end_dt and end_dt > booking_start_dt:
                raise ValidationError("This event space is already booked for the selected day and time. There must be at least 1 hour between two bookings.")

    def save(self, *args, **kwargs):
        """Call clean() before saving to enforce validation at the model level."""
        self.clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Booking by {self.resident} for '{self.event_space}' on {self.date} is {self.get_status_display()}"  # noqa


class ResidentRequest(models.Model):
    """
    """

    class Purpose(models.IntegerChoices):
        MAINTENANCE = 0, "Submit a maintenance request"
        MESSAGE = 1, "Message the community administrators"

    class Status(models.IntegerChoices):
        OPEN = 0, "Open"
        PROGRESS = 1, "In Progress"
        CLOSED = 2, "Closed"

    resident = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="resident_requests_by_user"
        )
    purpose = models.IntegerField(
        choices=Purpose.choices,
        default=Purpose.MAINTENANCE
        )
    urgent = models.BooleanField()
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(
        choices=Status.choices,
        default=Status.OPEN
        )

    def __str__(self):
        return f"{'Urgent' if self.urgent else ""} {'Maintenance Request' if self.purpose == 0 else 'Message'} by {self.resident} - {'Open' if self.status == 0 else 'In Progress' if self.status == 1 else 'Closed'}"  # noqa
