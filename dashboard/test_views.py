from django.urls import reverse
from django.test import TestCase
from django.contrib.auth.models import User


class TestSignUpViews(TestCase):
    """
    Test SignUp views containing MyCustomSignUpForm
    Only test parts that are customized
    Test that custom signup form is rendered
    Test submission of valid and invalid contact form
    """
    def test_render_signup_page_with_custom_form(self):
        """
        Verifies get request for signup page containing a custom signup form
        """
        # Send GET request and store response
        response = self.client.get(reverse('account_signup'))
        # Page is rendered correctly
        self.assertEqual(response.status_code, 200)
        # Customized content is rendered
        self.assertIn(b"To help identify you as a resident.", response.content)
        self.assertIn(
            b"Enter the email address you used in your SharedSpaces "
            b"resident contract.",
            response.content
            )

    # Test successful signup
    # No need to test unsuccessful signup since that is handled by
    # standard allauth with no customization
    def test_signup_successful(self):
        post_data = {
            "username": "testusername",
            "full_name": "test name",
            "email": "name@test.com",
            "password1": "testpassword",
            "password2": "testpassword",
        }
        response = self.client.post(reverse("account_signup"), post_data)

        # Check that redirects after signup
        self.assertEqual(response.status_code, 302)
        # Check that redirects to account inactive page
        self.assertRedirects(response, '/accounts/inactive/')

        # Check that user created
        self.assertTrue(User.objects.filter(username="testusername").exists())

        # Only check customized actions
        # Check that first name and last name saved correctly
        self.assertEqual(
            User.objects.get(username="testusername").first_name,
            "test"
            )
        self.assertEqual(
            User.objects.get(username="testusername").last_name,
            "name"
            )

        # Check that user set to inactive upon signup
        self.assertFalse(User.objects.get(username="testusername").is_active)


class TestLoginViews(TestCase):
    """
    Test Custom LoginView which checks that users which have an existing but
    inactive account are always redirected to the Account Inactive page when
    trying to sign in
    A active user is redirected to the Resident Space page
    """
    def setUp(self):
        # Create an inactive and an active user
        self.inactive_user = User.objects.create_user(
            username="inactiveusername",
            email="inactive@test.com",
            password="testpassword",
            is_active=False
        )
        self.active_user = User.objects.create_user(
            username="activeusername",
            email="active@test.com",
            password="testpassword",
            is_active=True
        )

    def test_redirect_inactive_user_to_account_inactive_page(self):
        """
        Verifies that inactive but existing user is redirected
        to account inactive page
        """
        response = self.client.post(
            reverse("account_login"),
            {"login": "inactiveusername", "password": "testpassword"}
            )
        # Page is redirected correctly
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Account Inactive", response.content)
        self.assertTemplateUsed(
            response,
            "../templates/account/account_inactive.html"
            )

    def test_active_login_successfully(self):
        """
        Verifies that active user can sign in and is redirected
        does not need to test further since is handled by standard allauth
        """
        response = self.client.post(
            reverse("account_login"),
            {"login": "activeusername", "password": "testpassword"}
            )
        # Page is redirected correctly
        self.assertEqual(response.status_code, 302)
