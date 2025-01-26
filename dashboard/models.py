from django.db import models
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

    def __str__(self):
        return f"Booking by {self.resident} for '{self.event_space}' on {self.date} is {self.get_status_display()}"  # noqa
