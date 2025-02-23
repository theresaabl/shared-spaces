from django.shortcuts import render
from django.urls import reverse
from django.contrib import messages
from .forms import ContactForm


def contact_page(request):
    """
    Display the contact page

    **Context**

    ``contact_messages``
        An instance of :model:`contact.ContactMessage`.

    **Template:**

    :template:`contact/contact.html`
    """

    # Start request.method is POST conditional
    if request.method == "POST":
        contact_form = ContactForm(data=request.POST)

        # Start contact form valid conditional
        if contact_form.is_valid():
            contact_form.save()

            contact_url = reverse('contact')
            messages.add_message(
                request, messages.SUCCESS,
                'Your message was successfully sent! '
                'If you do not hear back within 5 working days, please '
                f"""feel free to <a href="{contact_url}">contact us</a>."""
            )

        # booking form not valid:
        else:
            messages.add_message(
                request,
                messages.ERROR,
                'There was an error in your form. Please fill in again.'
            )

            return render(
                request,
                "contact/contact.html",
                {
                    "contact_form": contact_form,
                }
            )
        # End contact form valid conditional

    # if request.method is GET
    contact_form = ContactForm()

    return render(
        request,
        "contact/contact.html",
        {
            "contact_form": contact_form,
        }
    )
