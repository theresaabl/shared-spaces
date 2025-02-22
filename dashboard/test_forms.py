from django.test import TestCase, RequestFactory
from django.contrib.sessions.middleware import SessionMiddleware
from django.contrib.auth.models import User
from .forms import MyCustomSignupForm


class MyCustomSignupFormTest(TestCase):
    """
    Test allauth customized signup form
    Only check for fields that have customized (not passwords)
    """
    def setUp(self):
        # Create a fake request factory
        self.factory = RequestFactory()

    def test_form_is_valid(self):
        form_data = {
            'username': 'testusername',
            'full_name': 'test_firstname test_lastname',
            'email': 'name@test.com',
            "password1": "securepassword123",
            "password2": "securepassword123",
        }
        form = MyCustomSignupForm(data=form_data)
        self.assertTrue(form.is_valid(), msg='Form is invalid.')

    def test_form_is_invalid_username_missing(self):
        form_data = {
            'username': '',
            'full_name': 'test_firstname test_lastname',
            'email': 'name@test.com',
            "password1": "securepassword123",
            "password2": "securepassword123",
        }
        form = MyCustomSignupForm(data=form_data)
        self.assertFalse(
            form.is_valid(),
            msg='Username not provided, but form is valid.'
            )

    def test_form_is_invalid_username_invalid(self):
        form_data = {
            'username': 'test username',
            'full_name': 'test_firstname test_lastname',
            'email': 'name@test.com',
            "password1": "securepassword123",
            "password2": "securepassword123",
        }
        form = MyCustomSignupForm(data=form_data)
        self.assertFalse(
            form.is_valid(),
            msg='Username invalid, but form is valid.'
            )

    def test_form_is_invalid_name_missing(self):
        form_data = {
            'username': 'testusername',
            'full_name': '',
            'email': 'name@test.com',
            "password1": "securepassword123",
            "password2": "securepassword123",
        }
        form = MyCustomSignupForm(data=form_data)
        self.assertFalse(
            form.is_valid(),
            msg='Name not provided, but form is valid.'
            )

    def test_form_is_invalid_email_missing(self):
        form_data = {
            'username': 'testusername',
            'full_name': 'test_firstname test_lastname',
            'email': '',
            "password1": "securepassword123",
            "password2": "securepassword123",
        }
        form = MyCustomSignupForm(data=form_data)
        self.assertFalse(
            form.is_valid(),
            msg='Email not provided, but form is valid.'
            )

    def test_form_is_invalid_email_invalid(self):
        form_data = {
            'username': 'test username',
            'full_name': 'test_firstname test_lastname',
            'email': 'name email',
            "password1": "securepassword123",
            "password2": "securepassword123",
        }
        form = MyCustomSignupForm(data=form_data)
        self.assertFalse(
            form.is_valid(),
            msg='Email invalid, but form is valid.'
            )

    def test_form_is_invalid_email_invalid_dot(self):
        form_data = {
            'username': 'test username',
            'full_name': 'test_firstname test_lastname',
            'email': 'name@test',
            "password1": "securepassword123",
            "password2": "securepassword123",
        }
        form = MyCustomSignupForm(data=form_data)
        self.assertFalse(
            form.is_valid(),
            msg='Email missing dot, but form is valid.'
            )

    def test_form_is_invalid_email_invalid_at(self):
        form_data = {
            'username': 'test username',
            'full_name': 'test_firstname test_lastname',
            'email': 'test.com',
            "password1": "securepassword123",
            "password2": "securepassword123",
        }
        form = MyCustomSignupForm(data=form_data)
        self.assertFalse(
            form.is_valid(),
            msg='Email missing @, but form is valid.'
            )

    def test_save_method(self):
        """
        Test the save method
        Credits: To simulate a request and attach a session to it
                 ChatGPT was used for code inspiration
                 This does not directly test my code, but is necessary to
                 test custom code in save method
        """
        form_data = {
            'username': 'testusername',
            'full_name': 'test_firstname test_lastname',
            'email': 'name@test.com',
            "password1": "securepassword123",
            "password2": "securepassword123",
        }
        form = MyCustomSignupForm(data=form_data)

        # Validate form before calling save()
        self.assertTrue(form.is_valid())

        # Create a fake request
        request = self.factory.post("/accounts/signup/")

        # Attach session to the request
        # Create a middleware instance
        middleware = SessionMiddleware(lambda req: None)
        # Apply middleware to the request
        middleware.process_request(request)
        # Save session so it's accessible
        request.session.save()

        # Call save method with valid request
        user = form.save(request)

        # Check that the user was created correctly
        self.assertEqual(user.username, "testusername")
        # Full name split up into first and last name
        self.assertEqual(user.first_name, "test_firstname")
        self.assertEqual(user.last_name, "test_lastname")
        self.assertEqual(user.email, "name@test.com")

        # Check that user is inactive after signup
        self.assertFalse(user.is_active)

        # Ensure the user is saved in the database
        self.assertTrue(User.objects.filter(username="testusername").exists())
