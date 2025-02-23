import datetime
from django.test import TestCase, RequestFactory
from django.contrib.sessions.middleware import SessionMiddleware
from django.contrib.auth.models import User
from .forms import MyCustomSignupForm, BookingForm, ResidentRequestForm
from .models import EventSpace, EventSpaceBooking


class MyCustomSignupFormTest(TestCase):
    """
    Test allauth customized signup form
    Only check for fields that have customized (not passwords)
    Code inspiration to create fake requests and sessions
    (needed to test save method):
    request: https://docs.djangoproject.com/en/5.1/topics/testing/advanced/
    session: https://stackoverflow.com/a/55530933
    """
    def setUp(self):
        # set up request factory
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
        Code inspiration to create fake requests and sessions
        (needed to test save method):
        request: https://docs.djangoproject.com/en/5.1/topics/testing/advanced/
        session: https://stackoverflow.com/a/55530933
        """
        form_data = {
            'username': 'testusername',
            'full_name': 'test_firstname test_lastname',
            'email': 'name@test.com',
            "password1": "securepassword123",
            "password2": "securepassword123",
        }
        form = MyCustomSignupForm(data=form_data)

        # Validate form
        self.assertTrue(form.is_valid())

        # Fake POST request needed
        request = self.factory.post("/accounts/signup/")

        # Create fake session
        # placeholder function (that does nothing) as parameter
        # since a callable function is expected in SessionMiddleware.__init__()
        # but we do not have a real request/response
        middleware = SessionMiddleware(lambda request: None)
        middleware.process_request(request)
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


class TestBookingForm(TestCase):
    """
    Test Booking Form
    """
    def setUp(self):
        # Set up example event space
        self.event_space = EventSpace.objects.create(
            name="test space",
            type="test type",
            image="test image",
            building="test building",
            capacity="10",
            number_of_tables="10",
            number_of_chairs="10",
            kitchen="False",
            tea_and_coffeemaker="False",
            projector="False",
            audio_equipment="False",
            childrens_play_area="False",
            piano="False",
            notes="test notes"
            )
        # Create a user
        self.user = User.objects.create(
            username="testusername",
            password="testpassword",
            email="name@test.com"
        )
        # Set up one example booking so can test that
        # no duplicate bookings are allowed
        self.example_booking = EventSpaceBooking.objects.create(
            resident=self.user,
            event_space=self.event_space,
            occasion="test occasion",
            date="2025-10-18",
            # Convert string to time object:
            # https://stackoverflow.com/a/14295709
            # Need datetime.time object since calculations are done
            # during validation
            start=datetime.datetime.strptime('19:00', '%H:%M').time(),
            end=datetime.datetime.strptime('22:00', '%H:%M').time(),
            notes="test notes"
        )

    def test_form_is_valid(self):
        booking_form = BookingForm({
            'event_space': self.event_space.id,
            'occasion': 'test occasion',
            'date': '18/10/2025',
            'start': '10:00',
            'end': '12:00',
            'notes': 'test notes'
            })
        self.assertTrue(booking_form.is_valid(), msg="Form is invalid")

    # Check that notes are optional
    def test_form_is_valid_no_notes(self):
        booking_form = BookingForm({
            'event_space': self.event_space.id,
            'occasion': 'test occasion',
            'date': '18/10/2025',
            'start': '10:00',
            'end': '12:00',
            'notes': ''
            })
        self.assertTrue(
            booking_form.is_valid(),
            msg="No notes provided, form is invalid"
            )

    # Check that date format Y-m-d is also valid
    # (see settings DATE_INPUT_FORMATS)
    def test_form_is_valid_second_date_format(self):
        booking_form = BookingForm({
            'event_space': self.event_space.id,
            'occasion': 'test occasion',
            'date': '2025-10-18',
            'start': '10:00',
            'end': '12:00',
            'notes': 'test notes'
            })
        self.assertTrue(
            booking_form.is_valid(),
            msg="Y-m-d date provided, form is invalid"
            )

    # Check that form is invalid with missing fields
    # cannot test with missing start or end time since these are needed
    # for validation (in clean method of model)
    def test_form_is_invalid_missing_occasion(self):
        booking_form = BookingForm({
            'event_space': self.event_space.id,
            'occasion': '',
            'date': '10/18/2025',
            'start': '10:00',
            'end': '12:00',
            'notes': 'test notes'
            })
        self.assertFalse(
            booking_form.is_valid(),
            msg="No occasion provided, form is valid"
            )

    def test_form_is_invalid_missing_date(self):
        booking_form = BookingForm({
            'event_space': self.event_space.id,
            'occasion': 'test occasion',
            'date': '',
            'start': '10:00',
            'end': '12:00',
            'notes': 'test notes'
            })
        self.assertFalse(
            booking_form.is_valid(),
            msg="No date provided, form is valid"
            )

    # Check that form is invalid with invalid date format
    def test_form_is_invalid_invalid_date(self):
        booking_form = BookingForm({
            'event_space': self.event_space.id,
            'occasion': 'test occasion',
            'date': '10/18/2025',
            'start': '10:00',
            'end': '12:00',
            'notes': 'test notes'
            })
        self.assertFalse(
            booking_form.is_valid(),
            msg="Invalid date provided, form is valid"
            )

    # Check that form is invalid for checks done in the
    # clean method of the model
    # Check that form invalid if end time before start time
    def test_form_is_invalid_end_before_start(self):
        booking_form = BookingForm({
            'event_space': self.event_space.id,
            'occasion': 'test occasion',
            'date': '18/10/2025',
            'start': '10:00',
            'end': '09:00',
            'notes': 'test notes'
            })
        self.assertFalse(
            booking_form.is_valid(),
            msg="End time is before start time, form is valid"
            )

    # check that form invalid if duration less than one hour
    def test_form_is_invalid_short_duration(self):
        booking_form = BookingForm({
            'event_space': self.event_space.id,
            'occasion': 'test occasion',
            'date': '18/10/2025',
            'start': '10:00',
            'end': '10:30',
            'notes': 'test notes'
            })
        self.assertFalse(
            booking_form.is_valid(),
            msg="Duration of less than one hour, form is valid"
            )

    # check that no duplicate bookings are allowed
    # example booking: on 10/18/2025 from 19:00 - 22:00
    def test_form_is_invalid_duplicate_booking(self):
        booking_form = BookingForm({
            'event_space': self.event_space.id,
            'occasion': 'test occasion',
            'date': '18/10/2025',
            'start': '17:00',
            'end': '21:00',
            'notes': 'test notes'
            })
        self.assertFalse(
            booking_form.is_valid(),
            msg="There is already a booking on that date at that time, form is valid"  # noqa
            )

    # check that there must be at least one hour between bookings
    # example booking: on 10/18/2025 from 19:00 - 22:00
    def test_form_is_invalid_between_bookings(self):
        booking_form = BookingForm({
            'event_space': self.event_space.id,
            'occasion': 'test occasion',
            'date': '18/10/2025',
            'start': '15:00',
            'end': '18:30',
            'notes': 'test notes'
            })
        self.assertFalse(
            booking_form.is_valid(),
            msg="There is less than one hour between same day bookings, form is valid"  # noqa
            )

    # Check that form is valid if same day bookings at least one hour apart
    def test_form_is_valid_same_day(self):
        booking_form = BookingForm({
            'event_space': self.event_space.id,
            'occasion': 'test occasion',
            'date': '18/10/2025',
            'start': '12:00',
            'end': '18:00',
            'notes': 'test notes'
            })
        self.assertTrue(
            booking_form.is_valid(),
            msg="There is more than one hour between same day bookings, form is invalid"  # noqa
            )


class TestResidentRequestForm(TestCase):
    """
    Test Resident Request Form
    """
    def test_form_is_valid(self):
        res_request_form = ResidentRequestForm({
            'purpose': '0',
            'urgent': 'True',
            'content': 'test content',
            })
        self.assertTrue(res_request_form.is_valid(), msg="Form is invalid")

    # Check that form is invalid with empty fields
    def test_form_is_invalid_missing_purpose(self):
        res_request_form = ResidentRequestForm({
            'purpose': '',
            'urgent': 'True',
            'content': 'test content',
            })
        self.assertFalse(
            res_request_form.is_valid(),
            msg="Purpose not provided, but form is valid"
            )

    def test_form_is_invalid_missing_content(self):
        res_request_form = ResidentRequestForm({
            'purpose': '0',
            'urgent': 'False',
            'content': '',
            })
        self.assertFalse(
            res_request_form.is_valid(),
            msg="Content not provided, but form is valid"
            )

    # Check that form is invalid with invalid purpose
    def test_form_is_invalid_invalid_purpose(self):
        """
        Purpose is IntegerChoiceField
        """
        res_request_form = ResidentRequestForm({
            'purpose': 'test purpose',
            'urgent': 'False',
            'content': 'test content',
            })
        self.assertFalse(
            res_request_form.is_valid(),
            msg="Invalid purpose provided, but form is valid"
            )

    def test_form_is_invalid_invalid_purpose_int(self):
        """
        Purpose is IntegerChoiceField 0, 1, 2
        """
        res_request_form = ResidentRequestForm({
            'purpose': '3',
            'urgent': 'False',
            'content': 'test content',
            })
        self.assertFalse(
            res_request_form.is_valid(),
            msg="Invalid purpose provided, but form is valid"
            )
