from django.db import models


class ContactMessage(models.Model):
    """
    """
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    interest_to_join = models.BooleanField()
    message = models.TextField()
    sent_on = models.DateTimeField(auto_now_add=True)
    processed = models.BooleanField()

    def __str__(self):
        return f"Contact message by {self.name}{' with interest to join.' if self.interest_to_join else ''}"  # noqa
