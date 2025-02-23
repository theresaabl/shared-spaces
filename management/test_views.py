import datetime
from django.urls import reverse
from django.test import TestCase
from django.contrib.auth.models import User
from contact.models import ContactMessage
from dashboard.models import EventSpace, EventSpaceBooking, ResidentRequest
from .forms import EventSpaceForm


class TestManagementPageView(TestCase):
    """
    Test management page view
    Test that management page is rendered for staff users
    Redirected for non staff users
    """
    def setUp(self):
        # Create Superuser
        self.superuser = User.objects.create_superuser(
            username="superusername",
            password="testpassword"
        )
        # Create normal user
        self.user = User.objects.create_user(
            username="testusername",
            password="testpassword",
        )

    def test_render_management_page_for_staff(self):
        # login as superuser
        self.client.login(username="superusername", password="testpassword")
        response = self.client.get(reverse('management'))
        # Page is rendered correctly
        self.assertEqual(response.status_code, 200)
        # Check content for staff users
        self.assertIn(b"Admin Space", response.content)
        self.assertIn(b"User Accounts", response.content)

    def test_not_render_management_page_for_non_staff(self):
        # login as normal user
        self.client.login(username="testusername", password="testpassword")
        response = self.client.get(reverse('management'))
        # Check Redirect
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/admin/login/?next=/management/')

    def test_not_render_management_page_for_nonauthenticated_user(self):
        response = self.client.get(reverse('management'))
        # Check Redirect
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/admin/login/?next=/management/')


class TestUserAccountsView(TestCase):
    """
    Test user accounts page view
    Test that different types of users are displayed correctly
    """
    def setUp(self):
        # Create Superuser
        self.superuser = User.objects.create_superuser(
            username="superusername",
            first_name="Super",
            last_name="User",
            email="superuser@test.com",
            password="testpassword",
        )
        # Create normal user
        self.user = User.objects.create_user(
            username="testusername",
            first_name="Normal",
            last_name="User",
            email="user@test.com",
            password="testpassword",
        )
        # Create inactive user
        self.inactiveuser = User.objects.create_user(
            username="inactiveusername",
            first_name="Inactive",
            last_name="User",
            email="inactiveuser@test.com",
            password="testpassword",
        )
        self.inactiveuser.is_active = False
        self.inactiveuser.save()

    def test_render_user_page_for_staff_with_content(self):
        # login as superuser
        self.client.login(username="superusername", password="testpassword")
        response = self.client.get(reverse('mgmt-users'))
        # Page is rendered correctly
        self.assertEqual(response.status_code, 200)
        # Check content for logged in users
        self.assertIn(b"superusername", response.content)
        self.assertIn(b"Name: Super User", response.content)
        self.assertIn(b"Email: superuser@test.com", response.content)
        self.assertIn(b"testusername", response.content)
        self.assertIn(b"Name: Normal User", response.content)
        self.assertIn(b"Email: user@test.com", response.content)
        self.assertIn(b"inactiveusername", response.content)
        self.assertIn(b"Name: Inactive User", response.content)
        self.assertIn(b"Email: inactiveuser@test.com", response.content)

    def test_not_render_user_page_for_non_staff(self):
        # login as normal user
        self.client.login(username="testusername", password="testpassword")
        response = self.client.get(reverse('mgmt-users'))
        # Check Redirect
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(
            response,
            '/admin/login/?next=/management/user-accounts/'
            )

    def test_not_render_user_page_for_nonauthenticated_user(self):
        response = self.client.get(reverse('mgmt-users'))
        # Check Redirect
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(
            response,
            '/admin/login/?next=/management/user-accounts/'
            )


class TestUserActivationView(TestCase):
    """
    Test user activation view
    Check that can change status from inactive to active and back
    Check that cannot deactivate own account
    """
    def setUp(self):
        # Create Superuser
        self.superuser = User.objects.create_superuser(
            username="superusername",
            first_name="Super",
            last_name="User",
            email="superuser@test.com",
            password="testpassword"
        )
        # Create normal user
        self.user = User.objects.create_user(
            username="testusername",
            first_name="Normal",
            last_name="User",
            email="user@test.com",
            password="testpassword",
        )
        # Create inactive user
        self.inactiveuser = User.objects.create_user(
            username="inactiveusername",
            first_name="Inactive",
            last_name="User",
            email="inactiveuser@test.com",
            password="testpassword",
        )
        self.inactiveuser.is_active = False
        self.inactiveuser.save()

    def test_successfully_activate_user(self):
        # login as super user
        self.client.login(username="superusername", password="testpassword")
        # check that inactive user is indeed inactive
        self.assertFalse(self.inactiveuser.is_active)
        response = self.client.get(
            reverse('mgmt-user-activation', args=(self.inactiveuser.id,)),
            follow=True
            )
        # Follow Redirect to check page is rendered and messages displayed
        self.assertEqual(response.status_code, 200)
        self.assertIn(
            b"User account successfully activated!",
            response.content
            )

    def test_successfully_deactivate_user(self):
        # login as super user
        self.client.login(username="superusername", password="testpassword")
        # check that active user is indeed active
        self.assertTrue(self.user.is_active)
        response = self.client.get(
            reverse('mgmt-user-activation', args=(self.user.id,)),
            follow=True
            )
        # Follow Redirect to check page is rendered and messages displayed
        self.assertEqual(response.status_code, 200)
        self.assertIn(
            b"User account successfully deactivated!",
            response.content
            )

    def test_not_deactivate_own_user(self):
        # login as super user
        self.client.login(username="superusername", password="testpassword")
        # check that active user is indeed active
        self.assertTrue(self.superuser.is_active)
        response = self.client.get(
            reverse('mgmt-user-activation', args=(self.superuser.id,)),
            follow=True
            )
        # Follow Redirect to check page is rendered and messages displayed
        self.assertEqual(response.status_code, 200)
        self.assertIn(
            b"You cannot deactivate your own account!",
            response.content
            )


class TestUserAdminStatusView(TestCase):
    """
    Test user admin status view
    Check that can change admin status
    Check that cannot remove admin status from own account
    """
    def setUp(self):
        # Create Superuser
        self.superuser = User.objects.create_superuser(
            username="superusername",
            first_name="Super",
            last_name="User",
            email="superuser@test.com",
            password="testpassword"
        )
        # Create second Superuser
        self.superuser_2 = User.objects.create_superuser(
            username="superusername_2",
            first_name="Super2",
            last_name="User",
            email="super2user@test.com",
            password="testpassword"
        )
        # Create normal user
        self.user = User.objects.create_user(
            username="testusername",
            first_name="Normal",
            last_name="User",
            email="user@test.com",
            password="testpassword",
        )

    def test_successfully_give_admin_status(self):
        # login as super user
        self.client.login(username="superusername", password="testpassword")
        # check that user is indeed not staff
        self.assertFalse(self.user.is_staff)
        response = self.client.get(
            reverse('mgmt-user-admin-status', args=(self.user.id,)),
            follow=True
            )
        # Follow Redirect to check page is rendered and messages displayed
        self.assertEqual(response.status_code, 200)
        self.assertIn(
            b"Successfully added admin status!",
            response.content
            )

    def test_successfully_remove_admin_status(self):
        # login as super user
        self.client.login(username="superusername", password="testpassword")
        # check that superuser_2 is indeed staff
        self.assertTrue(self.superuser_2.is_staff)
        response = self.client.get(
            reverse('mgmt-user-admin-status', args=(self.superuser_2.id,)),
            follow=True
            )
        # Follow Redirect to check page is rendered and messages displayed
        self.assertEqual(response.status_code, 200)
        self.assertIn(
            b"Successfully removed admin status!",
            response.content
            )

    def test_not_remove_own_admin_status(self):
        # login as super user
        self.client.login(username="superusername", password="testpassword")
        response = self.client.get(
            reverse('mgmt-user-admin-status', args=(self.superuser.id,)),
            follow=True
            )
        # Follow Redirect to check page is rendered and messages displayed
        self.assertEqual(response.status_code, 200)
        self.assertIn(
            b"You cannot remove your own admin status!",
            response.content
            )


class TestUserDeleteView(TestCase):
    """
    Test user delete view
    Check that can delete users
    Check that cannot delete own account
    """
    def setUp(self):
        # Create Superuser
        self.superuser = User.objects.create_superuser(
            username="superusername",
            first_name="Super",
            last_name="User",
            email="superuser@test.com",
            password="testpassword"
        )
        # Create normal user
        self.user = User.objects.create_user(
            username="testusername",
            first_name="Normal",
            last_name="User",
            email="user@test.com",
            password="testpassword",
        )

    def test_successfully_delete_user(self):
        # login as super user
        self.client.login(username="superusername", password="testpassword")
        response = self.client.get(
            reverse('mgmt-user-delete', args=(self.user.id,)),
            follow=True
            )
        # Follow Redirect to check page is rendered and messages displayed
        self.assertEqual(response.status_code, 200)
        self.assertIn(
            b"User account successfully deleted!",
            response.content
            )

    def test_not_delete_own_user(self):
        # login as super user
        self.client.login(username="superusername", password="testpassword")
        response = self.client.get(
            reverse('mgmt-user-delete', args=(self.superuser.id,)),
            follow=True
            )
        # Follow Redirect to check page is rendered and messages displayed
        self.assertEqual(response.status_code, 200)
        self.assertIn(
            b"You cannot delete your own account!",
            response.content
            )


class TestEventSpacesView(TestCase):
    """
    Test event spaces view
    Test that content rendered correctly
    """
    def setUp(self):
        # Create Superuser
        self.superuser = User.objects.create_superuser(
            username="superusername",
            first_name="Super",
            last_name="User",
            email="superuser@test.com",
            password="testpassword"
        )

        # Create example event spaces
        self.event_space_1 = EventSpace.objects.create(
            name="test space 1",
            type="test type 1",
            image="test image",
            building="test building 1",
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

        self.event_space_2 = EventSpace.objects.create(
            name="test space 2",
            type="test type 2",
            image="test image",
            building="test building 2",
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

    def test_render_content_for_staff_users(self):
        self.client.login(username="superusername", password="testpassword")
        response = self.client.get(reverse('mgmt-event-spaces'))
        # Page is rendered correctly
        self.assertEqual(response.status_code, 200)
        # Check content for logged in users
        self.assertIn(b"Event Spaces", response.content)

        # Check that event spaces are displayed (check several fields)
        self.assertIn(b"test space 1", response.content)
        self.assertIn(b"test type 1", response.content)
        self.assertIn(b"test building 1", response.content)
        self.assertIn(b"test space 2", response.content)
        self.assertIn(b"test type 2", response.content)
        self.assertIn(b"test building 2", response.content)
        self.assertIn(b"Edit", response.content)

    def test_not_render_event_spaces_page_for_nonstaff(self):
        self.client.login(username="testusername", password="testpassword")
        response = self.client.get(reverse('mgmt-event-spaces'))
        # Check Redirect
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(
            response,
            '/admin/login/?next=/management/event-spaces/'
            )


class TestAddEventSpaceView(TestCase):
    """
    Test add event space view
    Render page with event space form
    Test successful and unsuccessful submission
    """
    def setUp(self):
        # Create Superuser
        self.superuser = User.objects.create_superuser(
            username="superusername",
            password="testpassword"
        )

    def test_not_render_edit_event_space_page_for_nonstaff(self):
        self.client.login(username="testusername", password="testpassword")
        response = self.client.get(reverse('mgmt-add-event-space'))
        # Check Redirect
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(
            response,
            '/admin/login/?next=/management/event-spaces/add-event-space'
            )

    def test_render_add_event_space_page_with_form(self):
        """
        Verifies get request for add event space page containing an
        event space form
        """
        self.client.login(username="superusername", password="testpassword")
        # Send GET request and store response
        response = self.client.get(reverse('mgmt-add-event-space'))
        # Page is rendered correctly
        self.assertEqual(response.status_code, 200)
        # The context is instance of correct form
        self.assertIsInstance(
            response.context['event_space_form'],
            EventSpaceForm
            )

    def test_successful_event_space_form_submission(self):
        """Test for submitting an event space form"""
        self.client.login(username="superusername", password="testpassword")
        post_data = {
            'name': 'test name',
            'type': 'test name',
            'image': 'test name',
            'building': 'test name',
            'capacity': '10',
            'number_of_tables': '10',
            'number_of_chairs': '10',
            'kitchen': True,
            'tea_and_coffeemaker': True,
            'projector': True,
            'audio_equipment': True,
            'childrens_play_area': True,
            'piano': True,
            'notes': 'test notes',
        }
        # follow=True can follow to redirected page and check content there
        response = self.client.post(
            reverse('mgmt-add-event-space'),
            post_data,
            follow=True
            )

        # Follow redirect to event spaces and check content
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"test name", response.content)
        self.assertIn(b"Capacity: 10", response.content)
        # Success message
        self.assertIn(
            b"You successfully added a new event space.",
            response.content
            )

    def test_unsuccessful_event_space_form_submission_missing_field(self):
        """Test for submitting an event space form with error"""
        self.client.login(username="superusername", password="testpassword")
        post_data = {
            'name': '',
            'type': 'test name',
            'image': 'test name',
            'building': 'test name',
            'capacity': '10',
            'number_of_tables': '10',
            'number_of_chairs': '10',
            'kitchen': True,
            'tea_and_coffeemaker': True,
            'projector': True,
            'audio_equipment': True,
            'childrens_play_area': True,
            'piano': True,
            'notes': 'test notes',
        }
        # follow=True can follow to redirected page and check content there
        response = self.client.post(
            reverse('mgmt-add-event-space'),
            post_data,
            follow=True
            )

        # Follow redirect to event spaces and check content
        self.assertEqual(response.status_code, 200)
        # Success message
        self.assertIn(
            b"There was an error in your form.",
            response.content
            )


class TestEditEventSpaceView(TestCase):
    """
    Test edit event space view
    Render page with event space form
    Test successful and unsuccessful submission
    """
    def setUp(self):
        # Create Superuser
        self.superuser = User.objects.create_superuser(
            username="superusername",
            password="testpassword"
        )

        # Create example event spaces
        self.event_space = EventSpace.objects.create(
            name="test space",
            type="test type",
            image="test image",
            building="test building",
            capacity="10",
            number_of_tables="10",
            number_of_chairs="10",
            kitchen=True,
            tea_and_coffeemaker=True,
            projector=True,
            audio_equipment=True,
            childrens_play_area=True,
            piano=True,
            notes="test notes"
            )

    def test_not_render_add_event_space_page_for_nonstaff(self):
        self.client.login(username="testusername", password="testpassword")
        response = self.client.get(
            reverse('mgmt-edit-event-space', args=(self.event_space.id,)),
            )
        # Check Redirect
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(
            response,
            '/admin/login/?next=/management/event-spaces/edit-event-space/1'
            )

    def test_render_edit_event_space_page_with_form(self):
        """
        Verifies get request for edit event space page containing an
        event space form which is prefilled
        """
        self.client.login(username="superusername", password="testpassword")
        # Send GET request and store response
        response = self.client.get(
            reverse('mgmt-edit-event-space', args=(self.event_space.id,)),
            )
        # Page is rendered correctly
        self.assertEqual(response.status_code, 200)
        # The context is instance of correct form
        self.assertIsInstance(
            response.context['event_space_form'],
            EventSpaceForm
            )
        # Check that form is prefilled
        self.assertIn(b"test space", response.content)
        self.assertIn(b"test type", response.content)
        self.assertIn(b"test building", response.content)

    def test_successful_event_space_form_edit(self):
        """Test for editing an event space form"""
        self.client.login(username="superusername", password="testpassword")
        post_data = {
            'name': 'test space changed',
            'type': 'test type',
            'image': 'test image',
            'building': 'test building',
            'capacity': '10',
            'number_of_tables': '10',
            'number_of_chairs': '10',
            'kitchen': True,
            'tea_and_coffeemaker': True,
            'projector': True,
            'audio_equipment': True,
            'childrens_play_area': True,
            'piano': True,
            'notes': 'test notes',
        }
        response = self.client.post(
            reverse('mgmt-edit-event-space', args=(self.event_space.id,)),
            post_data,
            follow=True
            )

        # Follow redirect to event spaces and check content
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"test space changed", response.content)
        # Success message
        self.assertIn(
            b"Event Space was successfully updated!",
            response.content
            )

    def test_event_space_form_edit_no_change(self):
        """
        Test for editing an event space form with no change
        """
        self.client.login(username="superusername", password="testpassword")
        post_data = {
            'name': 'test space',
            'type': 'test type',
            'image': 'test image',
            'building': 'test building',
            'capacity': '10',
            'number_of_tables': '10',
            'number_of_chairs': '10',
            'kitchen': True,
            'tea_and_coffeemaker': True,
            'projector': True,
            'audio_equipment': True,
            'childrens_play_area': True,
            'piano': True,
            'notes': 'test notes',
        }
        response = self.client.post(
            reverse('mgmt-edit-event-space', args=(self.event_space.id,)),
            post_data,
            follow=True
            )

        # Follow redirect to event spaces and check content
        self.assertEqual(response.status_code, 200)
        # Info message
        self.assertIn(
            b"No changes were made to the event space.",
            response.content
            )

    def test_unsuccessful_event_space_form_edit(self):
        """
        Test for editing an event space form with error (missing capacity)
        (tested for each separate error in test_forms.py,
        here the view is important more than the form)
        """
        self.client.login(username="superusername", password="testpassword")
        post_data = {
            'name': 'test space',
            'type': 'test type',
            'image': 'test image',
            'building': 'test building',
            'capacity': '',
            'number_of_tables': '10',
            'number_of_chairs': '10',
            'kitchen': True,
            'tea_and_coffeemaker': True,
            'projector': True,
            'audio_equipment': True,
            'childrens_play_area': True,
            'piano': True,
            'notes': 'test notes',
        }
        response = self.client.post(
            reverse('mgmt-edit-event-space', args=(self.event_space.id,)),
            post_data
            )

        self.assertEqual(response.status_code, 200)
        # Error message
        self.assertIn(
            b"Error updating event space!",
            response.content
            )


class TestDeleteEventSpaceView(TestCase):
    """
    Test event space delete view
    Check that can delete event spaces
    """
    def setUp(self):
        # Create Superuser
        self.superuser = User.objects.create_superuser(
            username="superusername",
            password="testpassword"
        )

        # Create example event spaces
        self.event_space = EventSpace.objects.create(
            name="test space",
            type="test type",
            image="test image",
            building="test building",
            capacity="10",
            number_of_tables="10",
            number_of_chairs="10",
            kitchen=True,
            tea_and_coffeemaker=True,
            projector=True,
            audio_equipment=True,
            childrens_play_area=True,
            piano=True,
            notes="test notes"
            )

    def test_successfully_delete_event_space(self):
        # login as super user
        self.client.login(username="superusername", password="testpassword")
        response = self.client.get(
            reverse('mgmt-delete-event-space', args=(self.event_space.id,)),
            follow=True
            )
        # Follow Redirect to check page is rendered and messages displayed
        self.assertEqual(response.status_code, 200)
        self.assertIn(
            b"Event Space successfully deleted!",
            response.content
            )


class TestEventSpaceBookingsView(TestCase):
    """
    Test event space bookings page view
    Test that bookings are displayed correctly
    """
    def setUp(self):
        # Create Superuser
        self.superuser = User.objects.create_superuser(
            username="superusername",
            password="testpassword",
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

        # Create event space booking
        self.booking = EventSpaceBooking(
            resident=self.superuser,
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

    def test_render_booking_page_for_staff_with_content(self):
        # login as superuser
        self.client.login(username="superusername", password="testpassword")
        response = self.client.get(reverse('mgmt-event-space-bookings'))
        # Page is rendered correctly
        self.assertEqual(response.status_code, 200)
        # Check content for staff users
        self.assertIn(b"test space", response.content)
        self.assertIn(b"Resident: superusername", response.content)
        self.assertIn(b"Occasion: test occasion", response.content)

    def test_not_render_bookings_page_for_non_staff(self):
        # login as normal user
        self.client.login(username="testusername", password="testpassword")
        response = self.client.get(reverse('mgmt-event-space-bookings'))
        # Check Redirect
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(
            response,
            '/admin/login/?next=/management/event-space-bookings/'
            )


class TestApproveBookingView(TestCase):
    """
    Test approve booking view
    Check that can change status to approved
    Check that cannot approve already approved bookings
    Check that cannot approve past bookings
    """
    def setUp(self):
        # Create Superuser
        self.superuser = User.objects.create_superuser(
            username="superusername",
            password="testpassword",
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

        # Create event space booking
        self.booking = EventSpaceBooking(
            resident=self.superuser,
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

        # Create approved booking
        self.approved_booking = EventSpaceBooking(
            resident=self.superuser,
            event_space=self.event_space,
            occasion="test occasion",
            date="2025-10-20",
            start=datetime.datetime.strptime('19:00', '%H:%M').time(),
            end=datetime.datetime.strptime('22:00', '%H:%M').time(),
            notes="test notes",
            created_on=datetime.datetime.today(),
            status="1"
            )
        self.approved_booking.save()

        # Create past booking
        self.past_booking = EventSpaceBooking(
            resident=self.superuser,
            event_space=self.event_space,
            occasion="test occasion",
            date="2024-10-20",
            start=datetime.datetime.strptime('19:00', '%H:%M').time(),
            end=datetime.datetime.strptime('22:00', '%H:%M').time(),
            notes="test notes",
            created_on=datetime.datetime.today(),
            status="0"
            )
        self.past_booking.save()

    def test_successfully_approve_booking(self):
        # login as super user
        self.client.login(username="superusername", password="testpassword")
        # check that pending booking is indeed pending
        self.assertEqual(self.booking.status, "0")
        response = self.client.get(
            reverse('mgmt-booking-approve', args=(self.booking.id,)),
            follow=True
            )
        # Follow Redirect to check page is rendered and messages displayed
        self.assertEqual(response.status_code, 200)
        self.assertIn(
            b"Booking successfully approved!",
            response.content
            )

    def test_not_approve_approved_booking(self):
        # login as super user
        self.client.login(username="superusername", password="testpassword")
        # check that approved booking is indeed approved
        self.assertEqual(self.approved_booking.status, "1")
        response = self.client.get(
            reverse('mgmt-booking-approve', args=(self.approved_booking.id,)),
            follow=True
            )
        # Follow Redirect to check page is rendered and messages displayed
        self.assertEqual(response.status_code, 200)
        self.assertIn(
            b"This booking was already approved!",
            response.content
            )

    def test_not_approve_past_booking(self):
        # login as super user
        self.client.login(username="superusername", password="testpassword")
        response = self.client.get(
            reverse('mgmt-booking-approve', args=(self.past_booking.id,)),
            follow=True
            )
        # Follow Redirect to check page is rendered and messages displayed
        self.assertEqual(response.status_code, 200)
        self.assertIn(
            b"You cannot change the status of past bookings!",
            response.content
            )


class TestDenyBookingView(TestCase):
    """
    Test deny booking view
    Check that can change status to denied
    Check that cannot deny already denied bookings
    Check that cannot deny past bookings
    """
    def setUp(self):
        # Create Superuser
        self.superuser = User.objects.create_superuser(
            username="superusername",
            password="testpassword",
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

        # Create event space booking
        self.booking = EventSpaceBooking(
            resident=self.superuser,
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

        # Create approved booking
        self.denied_booking = EventSpaceBooking(
            resident=self.superuser,
            event_space=self.event_space,
            occasion="test occasion",
            date="2025-10-20",
            start=datetime.datetime.strptime('19:00', '%H:%M').time(),
            end=datetime.datetime.strptime('22:00', '%H:%M').time(),
            notes="test notes",
            created_on=datetime.datetime.today(),
            status="2"
            )
        self.denied_booking.save()

        # Create past booking
        self.past_booking = EventSpaceBooking(
            resident=self.superuser,
            event_space=self.event_space,
            occasion="test occasion",
            date="2024-10-20",
            start=datetime.datetime.strptime('19:00', '%H:%M').time(),
            end=datetime.datetime.strptime('22:00', '%H:%M').time(),
            notes="test notes",
            created_on=datetime.datetime.today(),
            status="0"
            )
        self.past_booking.save()

    def test_successfully_deny_booking(self):
        # login as super user
        self.client.login(username="superusername", password="testpassword")
        response = self.client.get(
            reverse('mgmt-booking-deny', args=(self.booking.id,)),
            follow=True
            )
        # Follow Redirect to check page is rendered and messages displayed
        self.assertEqual(response.status_code, 200)
        self.assertIn(
            b"Booking successfully denied!",
            response.content
            )

    def test_not_deny_denied_booking(self):
        # login as super user
        self.client.login(username="superusername", password="testpassword")
        response = self.client.get(
            reverse('mgmt-booking-deny', args=(self.denied_booking.id,)),
            follow=True
            )
        # Follow Redirect to check page is rendered and messages displayed
        self.assertEqual(response.status_code, 200)
        self.assertIn(
            b"This booking was already denied!",
            response.content
            )

    def test_not_deny_past_booking(self):
        # login as super user
        self.client.login(username="superusername", password="testpassword")
        response = self.client.get(
            reverse('mgmt-booking-deny', args=(self.past_booking.id,)),
            follow=True
            )
        # Follow Redirect to check page is rendered and messages displayed
        self.assertEqual(response.status_code, 200)
        self.assertIn(
            b"You cannot change the status of past bookings!",
            response.content
            )

#     def test_successfully_deactivate_user(self):
#         # login as super user
#         self.client.login(username="superusername", password="testpassword")
#         # check that active user is indeed active
#         self.assertTrue(self.user.is_active)
#         response = self.client.get(
#             reverse('mgmt-user-activation', args=(self.user.id,)),
#             follow=True
#             )
#         # Follow Redirect to check page is rendered and messages displayed
#         self.assertEqual(response.status_code, 200)
#         self.assertIn(
#             b"User account successfully deactivated!",
#             response.content
#             )

#     def test_not_deactivate_own_user(self):
#         # login as super user
#         self.client.login(username="superusername", password="testpassword")
#         # check that active user is indeed active
#         self.assertTrue(self.superuser.is_active)
#         response = self.client.get(
#             reverse('mgmt-user-activation', args=(self.superuser.id,)),
#             follow=True
#             )
#         # Follow Redirect to check page is rendered and messages displayed
#         self.assertEqual(response.status_code, 200)
#         self.assertIn(
#             b"You cannot deactivate your own account!",
#             response.content
#             )

