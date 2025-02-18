import datetime
from django import forms
from allauth.account.forms import SignupForm
from .models import EventSpaceBooking, ResidentRequest


class MyCustomSignupForm(SignupForm):
    """
    Add custom fields to the allauth Sign Up form
    Add first and last name
    Set all users to inactive when first signing up (admin can set to active)
    Code inspiration from: https://stackoverflow.com/a/25797705
    adapted with: https://docs.allauth.org/en/dev/account/forms.html
    """
    username = forms.CharField(
        max_length=200,
        required=True,
        widget=forms.TextInput(attrs={"placeholder": "Username"})
        )
    full_name = forms.CharField(
        max_length=200,
        widget=forms.TextInput(attrs={"placeholder": "Full Name"}),
        help_text="To help identify you as a resident."
        )
    email = forms.EmailField(
        max_length=200,
        required=True,
        widget=forms.TextInput(attrs={"placeholder": "Email address"}),
        help_text="Enter the email address you used "
                  "in your SharedSpaces resident contract."
        )

    field_order = ["username", "full_name", "email"]

    def save(self, request):

        # Ensure you call the parent class's save.
        # .save() returns a User object.
        user = super(MyCustomSignupForm, self).save(request)

        full_name_list = self.cleaned_data['full_name'].rsplit(" ", 1)
        user.first_name = full_name_list[0]
        user.last_name = full_name_list[1]

        # set user to inactive each time a new user signs up
        user.is_active = False

        user.save()

        # You must return the original result.
        return user


class BookingForm(forms.ModelForm):
    class Meta:
        model = EventSpaceBooking
        fields = ('event_space', 'occasion', 'date', 'start', 'end', 'notes',)
        # choose how input fields are rendered in html, date and time pickers
        widgets = {
            # only allow dates from tomorrow on (only bookings in the future)
            'date': forms.DateInput(
                attrs={'type': 'date', 'min': (datetime.date.today() + datetime.timedelta(days=1)), 'id': 'booking-date'},
                format="%d/%m/%Y"  # This is how date is rendered
                ),
            'start': forms.TimeInput(attrs={'type': 'time'}),
            'end': forms.TimeInput(attrs={'type': 'time'}),
        }


class ResidentRequestForm(forms.ModelForm):
    class Meta:
        model = ResidentRequest
        fields = ('purpose', 'urgent', 'content',)
