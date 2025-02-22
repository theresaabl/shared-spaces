from django.urls import reverse
from django.test import TestCase
from .forms import ContactForm


class TestContactViews(TestCase):
    """
    Test contact views
    There is no mock data to set up
    Test that contact form is rendered
    """
    def test_render_contact_page_with_contact_form(self):
        """Verifies get request for contact page containing a contact form"""
        # Send GET request and store response
        response = self.client.get(reverse('contact'))
        # Page is rendered correctly
        self.assertEqual(response.status_code, 200)
        # The context is instance of correct form
        self.assertIsInstance(response.context['contact_form'], ContactForm)

    def test_successful_contact_message_submission(self):
        """Test for sending a contact message"""
        post_data = {
            'name': 'test name',
            'email': 'name@test.com',
            'interest_to_join': 'False',
            'message': 'This is a test message.'
        }
        response = self.client.post(reverse('contact'), post_data)
        self.assertEqual(response.status_code, 200)
        self.assertIn(
            b'Your message was successfully sent!',
            response.content
        )

    def test_invalid_contact_message_submission(self):
        """Test for sending an invalid contact message"""
        post_data = {
            'name': 'test name',
            'email': '',
            'interest_to_join': 'False',
            'message': 'This is a test message.'
        }
        response = self.client.post(reverse('contact'), post_data)
        self.assertEqual(response.status_code, 200)
        self.assertIn(
            b'There was an error in your form.',
            response.content
        )
