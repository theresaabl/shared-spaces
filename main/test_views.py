from django.urls import reverse
from django.test import TestCase


class TestMainViews(TestCase):
    """
    Test main views
    Test that home page and about section are rendered correctly
    """
    def test_render_home_page(self):
        """Verifies get request for home page"""
        # Send GET request and store response
        response = self.client.get(reverse('home'))
        # Page is rendered correctly
        self.assertEqual(response.status_code, 200)

    def test_redirect_to_about_section(self):
        """Verifies get request for about section"""
        # Send GET request and store response
        response = self.client.get(reverse('about'))
        # Section is redirected correctly, 302 = Redirect
        self.assertEqual(response.status_code, 302)
        # Redirected to correct url
        self.assertRedirects(response, "/#about-section")
