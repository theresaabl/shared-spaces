from django import forms
from allauth.account.forms import SignupForm


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

        user.full_name = self.cleaned_data['full_name']
        user.is_active = False

        user.save()

        # You must return the original result.
        return user
