import datetime
from django.urls import reverse
from django.test import TestCase
from django.contrib.auth.models import User
from .models import EventSpace, EventSpaceBooking, ResidentRequest
from .forms import BookingForm


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

    def test_active_user_login_successfully(self):
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


class TestResidentSpaceViews(TestCase):
    """
    Test resident space views
    Test that resident space page is rendered for authenticated users
    Different content for not authenticated users
    """
    def setUp(self):
        # Create User
        self.user = User.objects.create_user(
            username="testusername",
            email="name@test.com",
            password="testpassword",
            is_active=True
        )
        # Create example event space
        self.event_space = EventSpace.objects.create(
            name="test space",
            type="test type",
            image="test image",
            building="test building",
            capacity="10",
            number_of_tables="10",
            number_of_chairs="10",
            kitchen=False,
            tea_and_coffeemaker=False,
            projector=False,
            audio_equipment=False,
            childrens_play_area=False,
            piano=False,
            notes="test notes"
            )
        # Create event space bookings
        self.booking = EventSpaceBooking(
            resident=self.user,
            event_space=self.event_space,
            occasion="test occasion",
            date="2025-10-18",
            start=datetime.datetime.strptime('19:00', '%H:%M').time(),
            end=datetime.datetime.strptime('22:00', '%H:%M').time(),
            notes="test notes",
            created_on=datetime.datetime.today(),
            status="0"
            )
        self.booking.save()

        # Create resident requests
        self.res_maint_request = ResidentRequest(
            resident=self.user,
            purpose="0",
            urgent=True,
            content="test maintenance request",
            created_on=datetime.datetime.today(),
            status="0"
            )
        self.res_maint_request.save()

        self.res_message = ResidentRequest(
            resident=self.user,
            purpose="1",
            urgent=False,
            content="test message",
            created_on=datetime.datetime.today(),
            status="2"
            )
        self.res_message.save()

    def test_render_content_for_authenticated_users(self):
        self.client.login(username="testusername", password="testpassword")
        response = self.client.get(reverse('dashboard'))
        # Page is rendered correctly
        self.assertEqual(response.status_code, 200)
        # Check content for logged in users
        self.assertIn(b"Welcome to Your Resident Space", response.content)
        self.assertIn(b"testusername", response.content)

        # Check that event space bookings are displayed
        self.assertIn(b"test space", response.content)
        self.assertIn(b"test occasion", response.content)

        # Check that resident requests are displayed
        # For urgent maintenance request
        self.assertIn(b"Maintenance Request", response.content)
        self.assertIn(b"test maintenance request", response.content)
        self.assertIn(b"Urgent!", response.content)
        # For message
        self.assertIn(b"Message", response.content)
        self.assertIn(b"test message", response.content)

    def test_render_content_for_unauthenticated_users(self):
        response = self.client.get(reverse('dashboard'))
        # Page is rendered correctly
        self.assertEqual(response.status_code, 200)
        # Check content for not logged in users
        self.assertIn(b"You are not signed in !", response.content)


class TestEventSpaceBookingViews(TestCase):
    """
    Test event space booking view
    Render page with booking form
    Test successful and unsuccessful submission
    """
    def setUp(self):
        # Create User
        self.user = User.objects.create_user(
            username="testusername",
            email="name@test.com",
            password="testpassword",
            is_active=True
        )
        # Create example event space
        self.event_space = EventSpace.objects.create(
            name="test space",
            type="test type",
            image="test image",
            building="test building",
            capacity="10",
            number_of_tables="10",
            number_of_chairs="10",
            kitchen=False,
            tea_and_coffeemaker=False,
            projector=False,
            audio_equipment=False,
            childrens_play_area=False,
            piano=False,
            notes="test notes"
            )
        # Create event space bookings
        self.booking = EventSpaceBooking(
            resident=self.user,
            event_space=self.event_space,
            occasion="test occasion",
            date="2025-10-18",
            start=datetime.datetime.strptime('19:00', '%H:%M').time(),
            end=datetime.datetime.strptime('22:00', '%H:%M').time(),
            notes="test notes",
            created_on=datetime.datetime.today(),
            status="0"
            )
        self.booking.save()

    def test_not_render_booking_page_unauthenticated_user(self):
        """
        Verifies that unauthenticated users don't have access to booking page
        """
        # Send GET request and store response
        response = self.client.get(reverse('booking'))
        # Redirects correctly
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(
            response,
            '/accounts/login/?next=/dashboard/event_space_booking/'
            )

    def test_render_booking_page_with_booking_form(self):
        """
        Verifies get request for event space booking page containing a
        booking form
        """
        self.client.login(username="testusername", password="testpassword")
        # Send GET request and store response
        response = self.client.get(reverse('booking'))
        # Page is rendered correctly
        self.assertEqual(response.status_code, 200)
        # The context is instance of correct form
        self.assertIsInstance(
            response.context['booking_form'],
            BookingForm
            )

    def test_successful_booking_submission(self):
        """Test for submitting an event space booking"""
        self.client.login(username="testusername", password="testpassword")
        post_data = {
            'event_space': self.event_space.id,
            'occasion': 'test occasion',
            'date': '18/10/2025',
            'start': '10:00',
            'end': '12:00',
            'notes': 'test notes'
        }
        response = self.client.post(reverse('booking'), post_data)

        # Check that redirected back to dashboard
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('dashboard'))

    def test_unsuccessful_booking_submission_invalid_end_time(self):
        """
        Test for submitting an invalid event space booking
        end time earlier than start time
        """
        self.client.login(username="testusername", password="testpassword")
        post_data = {
            'event_space': self.event_space.id,
            'occasion': 'test occasion',
            'date': '18/10/2025',
            'start': '10:00',
            'end': '09:00',
            'notes': 'test notes'
        }
        response = self.client.post(reverse('booking'), post_data)

        # Check that stay on page and error message displayed
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Error booking event space!", response.content)
        self.assertIn(
            b"The end time must be later than the start time.",
            response.content
            )

    def test_unsuccessful_booking_submission_short_duration(self):
        """
        Test for submitting an invalid event space booking
        End time less than 1 hour after start time
        """
        self.client.login(username="testusername", password="testpassword")
        post_data = {
            'event_space': self.event_space.id,
            'occasion': 'test occasion',
            'date': '18/10/2025',
            'start': '10:00',
            'end': '10:30',
            'notes': 'test notes'
        }
        response = self.client.post(reverse('booking'), post_data)

        # Check that stay on page and error message displayed
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Error booking event space!", response.content)
        self.assertIn(
            b"The end time must be at least 1 hour after the start time.",
            response.content
            )

    def test_unsuccessful_booking_submission_duplicate_booking(self):
        """
        Test for submitting an invalid event space booking
        Another booking on the same day at the same time
        """
        self.client.login(username="testusername", password="testpassword")
        post_data = {
            'event_space': self.event_space.id,
            'occasion': 'test occasion',
            'date': '18/10/2025',
            'start': '17:00',
            'end': '21:30',
            'notes': 'test notes'
        }
        response = self.client.post(reverse('booking'), post_data)

        # Check that stay on page and error message displayed
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Error booking event space!", response.content)
        self.assertIn(
            b"This event space is already booked",
            response.content
            )

    def test_unsuccessful_booking_submission_close_booking(self):
        """
        Test for submitting an invalid event space booking
        Another booking on the same day less than one hour apart
        """
        self.client.login(username="testusername", password="testpassword")
        post_data = {
            'event_space': self.event_space.id,
            'occasion': 'test occasion',
            'date': '18/10/2025',
            'start': '13:00',
            'end': '18:30',
            'notes': 'test notes'
        }
        response = self.client.post(reverse('booking'), post_data)

        # Check that stay on page and error message displayed
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Error booking event space!", response.content)
        self.assertIn(
            b"This event space is already booked",
            response.content
            )


class TestEditEventSpaceBookingViews(TestCase):
    """
    Test edit event space booking view
    Render page with prefilled booking form
    Test successful and unsuccessful submission
    """
    def setUp(self):
        # Create two Users
        self.user_1 = User.objects.create_user(
            username="testusername_1",
            email="name1@test.com",
            password="testpassword",
            is_active=True
        )

        self.user_2 = User.objects.create_user(
            username="testusername_2",
            email="name2@test.com",
            password="testpassword",
            is_active=True
        )
        # Create example event space
        self.event_space = EventSpace.objects.create(
            name="test space",
            type="test type",
            image="test image",
            building="test building",
            capacity="10",
            number_of_tables="10",
            number_of_chairs="10",
            kitchen=False,
            tea_and_coffeemaker=False,
            projector=False,
            audio_equipment=False,
            childrens_play_area=False,
            piano=False,
            notes="test notes"
            )
        # Create event space bookings, one per user
        # User 1
        self.booking_1 = EventSpaceBooking(
            resident=self.user_1,
            event_space=self.event_space,
            occasion="test occasion 1",
            date="2025-10-18",
            start=datetime.datetime.strptime('19:00', '%H:%M').time(),
            end=datetime.datetime.strptime('22:00', '%H:%M').time(),
            notes="test notes",
            created_on=datetime.datetime.today(),
            status="0"
            )
        self.booking_1.save()

        # User 2
        self.booking_2 = EventSpaceBooking(
            resident=self.user_2,
            event_space=self.event_space,
            occasion="test occasion 2",
            date="2025-10-20",
            start=datetime.datetime.strptime('19:00', '%H:%M').time(),
            end=datetime.datetime.strptime('22:00', '%H:%M').time(),
            notes="test notes",
            created_on=datetime.datetime.today(),
            status="0"
            )
        self.booking_2.save()

        # Past Booking from User 1
        self.booking_3 = EventSpaceBooking(
            resident=self.user_1,
            event_space=self.event_space,
            occasion="test occasion 3",
            date="2024-10-20",
            start=datetime.datetime.strptime('19:00', '%H:%M').time(),
            end=datetime.datetime.strptime('22:00', '%H:%M').time(),
            notes="test notes",
            created_on=datetime.datetime.today(),
            status="0"
            )
        self.booking_3.save()

    def test_not_render_edit_booking_page_unauthenticated_user(self):
        """
        Verifies that unauthenticated users don't have access to edit booking page
        """
        # Send GET request and store response
        response = self.client.get(
            reverse('booking_edit', args=(self.booking_1.id,))
            )
        # Redirects correctly
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(
            response,
            '/accounts/login/?next=/dashboard/edit_booking/1'
            )

    def test_render_edit_booking_page_with_booking_form(self):
        """
        Verifies get request for edit event space booking page containing a
        booking form which is prefilled
        """
        # note specifiy which user!
        self.client.login(username="testusername_1", password="testpassword")
        # Send GET request and store response
        response = self.client.get(
            reverse('booking_edit', args=(self.booking_1.id,))
            )
        # Page is rendered correctly
        self.assertEqual(response.status_code, 200)
        # The context is instance of correct form
        self.assertIsInstance(
            response.context['booking_form'],
            BookingForm
            )
        # Check that form is prefilled
        self.assertIn(b"test space", response.content)
        self.assertIn(b"test occasion 1", response.content)

    def test_not_render_edit_booking_page_for_wrong_booking(self):
        """
        Verifies that user cannot access bookings from other users
        """
        # note specifiy which user!
        self.client.login(username="testusername_1", password="testpassword")
        # Send GET request and store response
        response = self.client.get(
            # booking_2 is booking from other user
            reverse('booking_edit', args=(self.booking_2.id,))
            )
        # Check redirect
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('dashboard'))

    def test_not_render_edit_booking_page_for_past_booking(self):
        """
        Verifies that user cannot access past bookings
        """
        # note specifiy which user!
        self.client.login(username="testusername_1", password="testpassword")
        # Send GET request and store response
        response = self.client.get(
            # booking_3 is past booking from this user
            reverse('booking_edit', args=(self.booking_3.id,))
            )
        # Check redirect
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('dashboard'))

    def test_successful_booking_edit(self):
        """Test for editing an event space booking (change date)"""
        self.client.login(username="testusername_1", password="testpassword")
        post_data = {
            'event_space': self.event_space.id,
            'occasion': 'test occasion 1',
            'date': '18/11/2025',
            'start': '19:00',
            'end': '22:00',
            'notes': 'test notes'
        }
        # With follow=True follows the redirect and can check content of the
        # page that is redirected to
        response = self.client.post(
            reverse('booking_edit', args=(self.booking_1.id,)),
            post_data,
            follow=True
            )

        # Check content of dashboard (focus on messages)
        self.assertEqual(response.status_code, 200)
        self.assertIn(
            b"Your booking was successfully updated!",
            response.content
            )

    def test_booking_not_changed(self):
        """Test for editing an event space booking with no change"""
        self.client.login(username="testusername_1", password="testpassword")
        post_data = {
            'event_space': self.event_space.id,
            'occasion': 'test occasion 1',
            'date': '18/10/2025',
            'start': '19:00',
            'end': '22:00',
            'notes': 'test notes'
        }
        # With follow=True follows the redirect and can check content of the
        # page that is redirected to
        response = self.client.post(
            reverse('booking_edit', args=(self.booking_1.id,)),
            post_data,
            follow=True
            )

        # Check content of dashboard (focus on messages)
        self.assertEqual(response.status_code, 200)
        self.assertIn(
            b"No changes were made to your booking.",
            response.content
            )

    def test_unsuccessful_booking_edit_invalid_end_time(self):
        """
        Test for editing an invalid event space booking
        end time earlier than start time
        """
        self.client.login(username="testusername_1", password="testpassword")
        post_data = {
            'event_space': self.event_space.id,
            'occasion': 'test occasion 1',
            'date': '18/10/2025',
            'start': '19:00',
            'end': '17:00',
            'notes': 'test notes'
        }
        response = self.client.post(
            reverse('booking_edit', args=(self.booking_1.id,)),
            post_data
            )

        # Check error messages are displayed
        self.assertEqual(response.status_code, 200)
        self.assertIn(
            b"Error updating event space booking!",
            response.content
            )
        self.assertIn(
            b"The end time must be later than the start time.",
            response.content
            )

    def test_unsuccessful_booking_edit_short_duration(self):
        """
        Test for editing an invalid event space booking
        short duration
        """
        self.client.login(username="testusername_1", password="testpassword")
        post_data = {
            'event_space': self.event_space.id,
            'occasion': 'test occasion 1',
            'date': '18/10/2025',
            'start': '19:00',
            'end': '19:30',
            'notes': 'test notes'
        }
        response = self.client.post(
            reverse('booking_edit', args=(self.booking_1.id,)),
            post_data
            )

        # Check error messages are displayed
        self.assertEqual(response.status_code, 200)
        self.assertIn(
            b"Error updating event space booking!",
            response.content
            )
        self.assertIn(
            b"The end time must be at least 1 hour after the start time.",
            response.content
            )

    def test_unsuccessful_booking_edit_duplicate_booking(self):
        """
        Test for editing an invalid event space booking
        duplicate booking (overlapping with booking_2)
        """
        self.client.login(username="testusername_1", password="testpassword")
        post_data = {
            'event_space': self.event_space.id,
            'occasion': 'test occasion 1',
            'date': '20/10/2025',
            'start': '17:00',
            'end': '21:30',
            'notes': 'test notes'
        }
        response = self.client.post(
            reverse('booking_edit', args=(self.booking_1.id,)),
            post_data
            )

        # Check error messages are displayed
        self.assertEqual(response.status_code, 200)
        self.assertIn(
            b"Error updating event space booking!",
            response.content
            )
        self.assertIn(
            b"This event space is already booked",
            response.content
            )

    def test_unsuccessful_booking_edit_close_booking(self):
        """
        Test for editing an invalid event space booking
        booking less than 1 hour from booking_2
        """
        self.client.login(username="testusername_1", password="testpassword")
        post_data = {
            'event_space': self.event_space.id,
            'occasion': 'test occasion 1',
            'date': '20/10/2025',
            'start': '15:00',
            'end': '18:30',
            'notes': 'test notes'
        }
        response = self.client.post(
            reverse('booking_edit', args=(self.booking_1.id,)),
            post_data
            )

        # Check error messages are displayed
        self.assertEqual(response.status_code, 200)
        self.assertIn(
            b"Error updating event space booking!",
            response.content
            )
        self.assertIn(
            b"This event space is already booked",
            response.content
            )
