import datetime
from django import forms
from allauth.account.forms import SignupForm
from .models import EventSpaceBooking, ResidentRequest


class MyCustomSignupForm(SignupForm):
    """
    Add custom fields to the allauth Sign Up form
    Add full name
    Set all users to inactive when first signing up (admin can activate)
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
        widget=forms.TextInput(
            attrs={"placeholder": "Full Name", 'autocomplete': 'name'}
            ),
        help_text="To help identify you as a resident."
        )
    email = forms.EmailField(
        max_length=200,
        required=True,
        widget=forms.TextInput(
            attrs={"placeholder": "Email address", 'autocomplete': 'email'}
            ),
        help_text="Enter the email address you used "
                  "in your SharedSpaces resident contract."
        )

    field_order = ["username", "full_name", "email"]

    def save(self, request):

        # Ensure you call the parent class's save.
        # .save() returns a User object.
        user = super(MyCustomSignupForm, self).save(request)

        # correctly save first and last name
        full_name_list = self.cleaned_data['full_name'].rsplit(" ", 1)
        user.first_name = full_name_list[0]
        user.last_name = full_name_list[1]

        # Important! set user to inactive each time a new user signs up
        user.is_active = False

        user.save()

        # You must return the original result.
        return user


class BookingForm(forms.ModelForm):
    """
    Form for creating event space bookings
    Based on the EventSpaceBooking model

    Fields:
        - event_space (ForeignKey related to :model:`dashboard.EventSpace`)
        - occasion (CharField)
        - date (DateField)
        - start (TimeField)
        - end (TimeField)
        - notes (TextField, optional)
    """
    class Meta:
        model = EventSpaceBooking
        fields = ('event_space', 'occasion', 'date', 'start', 'end', 'notes',)
        # choose how input fields are rendered in html, date and time pickers
        widgets = {
            # only allow dates from tomorrow on (only bookings in the future)
            'date': forms.DateInput(
                attrs={
                    'type': 'date',
                    'min': (datetime.date.today() + datetime.timedelta(days=1))
                    },
                format="%d/%m/%Y"  # This is how date is rendered
                ),
            'start': forms.TimeInput(attrs={'type': 'time'}),
            'end': forms.TimeInput(attrs={'type': 'time'}),
        }


class ResidentRequestForm(forms.ModelForm):
    """
    Form for creating resident requests
    Based on the ResidentRequest model

    Fields:
        - purpose (IntegerChoice)
        - urgent (BooleanField)
        - content (TextField)
    """
    class Meta:
        model = ResidentRequest
        fields = ('purpose', 'urgent', 'content',)
