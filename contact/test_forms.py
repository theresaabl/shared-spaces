from django.test import TestCase
from .forms import ContactForm


class TestContactForm(TestCase):
    """
    Test Contact Form
    """
    def test_form_is_valid(self):
        contact_form = ContactForm({
            'name': 'test name',
            'email': 'name@text.com',
            'interest_to_join': True,
            'message': 'This is a nice message.'
            })
        self.assertTrue(contact_form.is_valid(), msg="Form is invalid")

    def test_form_is_invalid_name_missing(self):
        contact_form = ContactForm({
            'name': '',
            'email': 'name@text.com',
            'interest_to_join': True,
            'message': 'This is a nice message.'
            })
        self.assertFalse(
            contact_form.is_valid(),
            msg="Name not provided, but form is valid"
            )

    def test_form_is_invalid_email_missing(self):
        contact_form = ContactForm({
            'name': 'test name',
            'email': '',
            'interest_to_join': True,
            'message': 'This is a nice message.'
            })
        self.assertFalse(
            contact_form.is_valid(),
            msg="Email not provided, but form is valid"
            )

    def test_form_is_invalid_email_invalid(self):
        contact_form = ContactForm({
            'name': 'test name',
            'email': 'test email',
            'interest_to_join': True,
            'message': 'This is a nice message.'
            })
        self.assertFalse(
            contact_form.is_valid(),
            msg="Email not an email address, but form is valid"
            )

    def test_form_is_invalid_email_invalid_dot(self):
        contact_form = ContactForm({
            'name': 'test name',
            'email': 'name@test',
            'interest_to_join': True,
            'message': 'This is a nice message.'
            })
        self.assertFalse(
            contact_form.is_valid(),
            msg="Email missing dot, but form is valid"
            )

    def test_form_is_invalid_email_invalid_at(self):
        contact_form = ContactForm({
            'name': 'test name',
            'email': 'test.com',
            'interest_to_join': True,
            'message': 'This is a nice message.'
            })
        self.assertFalse(
            contact_form.is_valid(),
            msg="Email missing @, but form is valid"
            )

    def test_form_is_invalid_message_missing(self):
        contact_form = ContactForm({
            'name': 'test name',
            'email': 'name@test.com',
            'interest_to_join': False,
            'message': ''
            })
        self.assertFalse(
            contact_form.is_valid(),
            msg="Message not provided, but form is valid"
            )
