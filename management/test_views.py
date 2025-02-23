from django.urls import reverse
from django.test import TestCase
from django.contrib.auth.models import User
from dashboard.models import EventSpace, EventSpaceBooking, ResidentRequest


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

    # def test_successfully_deactivate_user(self):
    #     # login as super user
    #     self.client.login(username="superusername", password="testpassword")
    #     response = self.client.get(
    #         reverse('mgmt-user-activation',  args=(self.user.id,)),
    #         )
    #     # Check Redirect
    #     self.assertEqual(response.status_code, 302)
    #     self.assertRedirects(
    #         response,
    #         '/management/user-accounts/'
    #         )
    #     # Check that user is inactive
    #     self.assertFalse(
    #         self.user.is_active
    #         )

    # def test_not_render_user_page_for_nonauthenticated_user(self):
    #     response = self.client.get(reverse('mgmt-users'))
    #     # Check Redirect
    #     self.assertEqual(response.status_code, 302)
    #     self.assertRedirects(
    #         response,
    #         '/admin/login/?next=/management/user-accounts/'
    #         )




# class TestEventSpaceBookingViews(TestCase):
#     """
#     Test event space booking view
#     Render page with booking form
#     Test successful and unsuccessful submission
#     """
# def setUp(self):
#         # Create User
#         self.user = User.objects.create_user(
#             username="testusername",
#             email="name@test.com",
#             password="testpassword",
#             is_active=True
#         )
#         # Create example event space
#         self.event_space = EventSpace.objects.create(
#             name="test space",
#             type="test type",
#             image="test image",
#             building="test building",
#             capacity="10",
#             number_of_tables="10",
#             number_of_chairs="10",
#             kitchen=False,
#             tea_and_coffeemaker=False,
#             projector=False,
#             audio_equipment=False,
#             childrens_play_area=False,
#             piano=False,
#             notes="test notes"
#             )
#         # Create event space bookings
#         self.booking = EventSpaceBooking(
#             resident=self.user,
#             event_space=self.event_space,
#             occasion="test occasion",
#             date="2025-10-18",
#             start=datetime.datetime.strptime('19:00', '%H:%M').time(),
#             end=datetime.datetime.strptime('22:00', '%H:%M').time(),
#             notes="test notes",
#             created_on=datetime.datetime.today(),
#             status="0"
#             )
#         self.booking.save()

#         # Create resident requests
#         self.res_maint_request = ResidentRequest(
#             resident=self.user,
#             purpose="0",
#             urgent=True,
#             content="test maintenance request",
#             created_on=datetime.datetime.today(),
#             status="0"
#             )
#         self.res_maint_request.save()

#         self.res_message = ResidentRequest(
#             resident=self.user,
#             purpose="1",
#             urgent=False,
#             content="test message",
#             created_on=datetime.datetime.today(),
#             status="2"
#             )
#         self.res_message.save()
#     def setUp(self):
#         # Create User
#         self.user = User.objects.create_user(
#             username="testusername",
#             email="name@test.com",
#             password="testpassword",
#             is_active=True
#         )
#         # Create example event space
#         self.event_space = EventSpace.objects.create(
#             name="test space",
#             type="test type",
#             image="test image",
#             building="test building",
#             capacity="10",
#             number_of_tables="10",
#             number_of_chairs="10",
#             kitchen=False,
#             tea_and_coffeemaker=False,
#             projector=False,
#             audio_equipment=False,
#             childrens_play_area=False,
#             piano=False,
#             notes="test notes"
#             )
#         # Create event space bookings
#         self.booking = EventSpaceBooking(
#             resident=self.user,
#             event_space=self.event_space,
#             occasion="test occasion",
#             date="2025-10-18",
#             start=datetime.datetime.strptime('19:00', '%H:%M').time(),
#             end=datetime.datetime.strptime('22:00', '%H:%M').time(),
#             notes="test notes",
#             created_on=datetime.datetime.today(),
#             status="0"
#             )
#         self.booking.save()

#     def test_not_render_booking_page_unauthenticated_user(self):
#         """
#         Verifies that unauthenticated users don't have access to booking page
#         """
#         # Send GET request and store response
#         response = self.client.get(reverse('booking'))
#         # Redirects correctly
#         self.assertEqual(response.status_code, 302)
#         self.assertRedirects(
#             response,
#             '/accounts/login/?next=/dashboard/event_space_booking/'
#             )

#     def test_render_booking_page_with_booking_form(self):
#         """
#         Verifies get request for event space booking page containing a
#         booking form
#         """
#         self.client.login(username="testusername", password="testpassword")
#         # Send GET request and store response
#         response = self.client.get(reverse('booking'))
#         # Page is rendered correctly
#         self.assertEqual(response.status_code, 200)
#         # The context is instance of correct form
#         self.assertIsInstance(
#             response.context['booking_form'],
#             BookingForm
#             )

#     def test_successful_booking_submission(self):
#         """Test for submitting an event space booking"""
#         self.client.login(username="testusername", password="testpassword")
#         post_data = {
#             'event_space': self.event_space.id,
#             'occasion': 'test occasion',
#             'date': '18/10/2025',
#             'start': '10:00',
#             'end': '12:00',
#             'notes': 'test notes'
#         }
#         # follow=True can follow to redirected page and check content there
#         response = self.client.post(reverse('booking'), post_data, follow=True)

#         self.assertEqual(response.status_code, 200)
#         self.assertIn(b"test occasion", response.content)
#         self.assertIn(b"test notes", response.content)
#         # Success message
#         self.assertIn(
#             b"You successfully sent a booking request.",
#             response.content
#             )

#     def test_unsuccessful_booking_submission_invalid_end_time(self):
#         """
#         Test for submitting an invalid event space booking
#         end time earlier than start time
#         """
#         self.client.login(username="testusername", password="testpassword")
#         post_data = {
#             'event_space': self.event_space.id,
#             'occasion': 'test occasion',
#             'date': '18/10/2025',
#             'start': '10:00',
#             'end': '09:00',
#             'notes': 'test notes'
#         }
#         response = self.client.post(reverse('booking'), post_data)

#         # Check that stay on page and error message displayed
#         self.assertEqual(response.status_code, 200)
#         self.assertIn(b"Error booking event space!", response.content)
#         self.assertIn(
#             b"The end time must be later than the start time.",
#             response.content
#             )

#     def test_unsuccessful_booking_submission_short_duration(self):
#         """
#         Test for submitting an invalid event space booking
#         End time less than 1 hour after start time
#         """
#         self.client.login(username="testusername", password="testpassword")
#         post_data = {
#             'event_space': self.event_space.id,
#             'occasion': 'test occasion',
#             'date': '18/10/2025',
#             'start': '10:00',
#             'end': '10:30',
#             'notes': 'test notes'
#         }
#         response = self.client.post(reverse('booking'), post_data)

#         # Check that stay on page and error message displayed
#         self.assertEqual(response.status_code, 200)
#         self.assertIn(b"Error booking event space!", response.content)
#         self.assertIn(
#             b"The end time must be at least 1 hour after the start time.",
#             response.content
#             )

#     def test_unsuccessful_booking_submission_duplicate_booking(self):
#         """
#         Test for submitting an invalid event space booking
#         Another booking on the same day at the same time
#         """
#         self.client.login(username="testusername", password="testpassword")
#         post_data = {
#             'event_space': self.event_space.id,
#             'occasion': 'test occasion',
#             'date': '18/10/2025',
#             'start': '17:00',
#             'end': '21:30',
#             'notes': 'test notes'
#         }
#         response = self.client.post(reverse('booking'), post_data)

#         # Check that stay on page and error message displayed
#         self.assertEqual(response.status_code, 200)
#         self.assertIn(b"Error booking event space!", response.content)
#         self.assertIn(
#             b"This event space is already booked",
#             response.content
#             )

#     def test_unsuccessful_booking_submission_close_booking(self):
#         """
#         Test for submitting an invalid event space booking
#         Another booking on the same day less than one hour apart
#         """
#         self.client.login(username="testusername", password="testpassword")
#         post_data = {
#             'event_space': self.event_space.id,
#             'occasion': 'test occasion',
#             'date': '18/10/2025',
#             'start': '13:00',
#             'end': '18:30',
#             'notes': 'test notes'
#         }
#         response = self.client.post(reverse('booking'), post_data)

#         # Check that stay on page and error message displayed
#         self.assertEqual(response.status_code, 200)
#         self.assertIn(b"Error booking event space!", response.content)
#         self.assertIn(
#             b"This event space is already booked",
#             response.content
#             )


# class TestEditEventSpaceBookingViews(TestCase):
#     """
#     Test edit event space booking view
#     Render page with prefilled booking form
#     Test successful and unsuccessful submission
#     Test that user does not have access to other users bookings
#     Test that user does not have access to past bookings
#     """
#     def setUp(self):
#         # Create two Users
#         self.user_1 = User.objects.create_user(
#             username="testusername_1",
#             email="name1@test.com",
#             password="testpassword",
#             is_active=True
#         )

#         self.user_2 = User.objects.create_user(
#             username="testusername_2",
#             email="name2@test.com",
#             password="testpassword",
#             is_active=True
#         )
#         # Create example event space
#         self.event_space = EventSpace.objects.create(
#             name="test space",
#             type="test type",
#             image="test image",
#             building="test building",
#             capacity="10",
#             number_of_tables="10",
#             number_of_chairs="10",
#             kitchen=False,
#             tea_and_coffeemaker=False,
#             projector=False,
#             audio_equipment=False,
#             childrens_play_area=False,
#             piano=False,
#             notes="test notes"
#             )
#         # Create event space bookings, one per user
#         # User 1
#         self.booking_1 = EventSpaceBooking(
#             resident=self.user_1,
#             event_space=self.event_space,
#             occasion="test occasion 1",
#             date="2025-10-18",
#             start=datetime.datetime.strptime('19:00', '%H:%M').time(),
#             end=datetime.datetime.strptime('22:00', '%H:%M').time(),
#             notes="test notes",
#             created_on=datetime.datetime.today(),
#             status="0"
#             )
#         self.booking_1.save()

#         # User 2
#         self.booking_2 = EventSpaceBooking(
#             resident=self.user_2,
#             event_space=self.event_space,
#             occasion="test occasion 2",
#             date="2025-10-20",
#             start=datetime.datetime.strptime('19:00', '%H:%M').time(),
#             end=datetime.datetime.strptime('22:00', '%H:%M').time(),
#             notes="test notes",
#             created_on=datetime.datetime.today(),
#             status="0"
#             )
#         self.booking_2.save()

#         # Past Booking from User 1
#         self.booking_3 = EventSpaceBooking(
#             resident=self.user_1,
#             event_space=self.event_space,
#             occasion="test occasion 3",
#             date="2024-10-20",
#             start=datetime.datetime.strptime('19:00', '%H:%M').time(),
#             end=datetime.datetime.strptime('22:00', '%H:%M').time(),
#             notes="test notes",
#             created_on=datetime.datetime.today(),
#             status="0"
#             )
#         self.booking_3.save()

#     def test_not_render_edit_booking_page_unauthenticated_user(self):
#         """
#         Verifies that unauthenticated users don't have access to
#         edit booking page
#         """
#         # Send GET request and store response
#         response = self.client.get(
#             reverse('booking_edit', args=(self.booking_1.id,))
#             )
#         # Redirects correctly
#         self.assertEqual(response.status_code, 302)
#         self.assertRedirects(
#             response,
#             '/accounts/login/?next=/dashboard/edit_booking/1'
#             )

#     def test_render_edit_booking_page_with_booking_form(self):
#         """
#         Verifies get request for edit event space booking page containing a
#         booking form which is prefilled
#         """
#         # note specifiy which user!
#         self.client.login(username="testusername_1", password="testpassword")
#         # Send GET request and store response
#         response = self.client.get(
#             reverse('booking_edit', args=(self.booking_1.id,))
#             )
#         # Page is rendered correctly
#         self.assertEqual(response.status_code, 200)
#         # The context is instance of correct form
#         self.assertIsInstance(
#             response.context['booking_form'],
#             BookingForm
#             )
#         # Check that form is prefilled
#         self.assertIn(b"test space", response.content)
#         self.assertIn(b"test occasion 1", response.content)

#     def test_not_render_edit_booking_page_for_wrong_booking(self):
#         """
#         Verifies that user cannot access bookings from other users
#         """
#         # note specifiy which user!
#         self.client.login(username="testusername_1", password="testpassword")
#         # Send GET request and store response
#         response = self.client.get(
#             # booking_2 is booking from other user
#             reverse('booking_edit', args=(self.booking_2.id,))
#             )
#         # Check redirect
#         self.assertEqual(response.status_code, 302)
#         self.assertRedirects(response, reverse('dashboard'))

#     def test_not_render_edit_booking_page_for_past_booking(self):
#         """
#         Verifies that user cannot access past bookings
#         """
#         # note specifiy which user!
#         self.client.login(username="testusername_1", password="testpassword")
#         # Send GET request and store response
#         response = self.client.get(
#             # booking_3 is past booking from this user
#             reverse('booking_edit', args=(self.booking_3.id,))
#             )
#         # Check redirect
#         self.assertEqual(response.status_code, 302)
#         self.assertRedirects(response, reverse('dashboard'))

#     def test_successful_booking_edit(self):
#         """Test for editing an event space booking (change date)"""
#         self.client.login(username="testusername_1", password="testpassword")
#         post_data = {
#             'event_space': self.event_space.id,
#             'occasion': 'test occasion 1',
#             'date': '18/11/2025',
#             'start': '19:00',
#             'end': '22:00',
#             'notes': 'test notes'
#         }
#         # With follow=True follows the redirect and can check content of the
#         # page that is redirected to
#         response = self.client.post(
#             reverse('booking_edit', args=(self.booking_1.id,)),
#             post_data,
#             follow=True
#             )

#         # Check content of dashboard (focus on messages)
#         self.assertEqual(response.status_code, 200)
#         self.assertIn(
#             b"Your booking was successfully updated!",
#             response.content
#             )

#     def test_booking_not_changed(self):
#         """Test for editing an event space booking with no change"""
#         self.client.login(username="testusername_1", password="testpassword")
#         post_data = {
#             'event_space': self.event_space.id,
#             'occasion': 'test occasion 1',
#             'date': '18/10/2025',
#             'start': '19:00',
#             'end': '22:00',
#             'notes': 'test notes'
#         }
#         # With follow=True follows the redirect and can check content of the
#         # page that is redirected to
#         response = self.client.post(
#             reverse('booking_edit', args=(self.booking_1.id,)),
#             post_data,
#             follow=True
#             )

#         # Check content of dashboard (focus on messages)
#         self.assertEqual(response.status_code, 200)
#         self.assertIn(
#             b"No changes were made to your booking.",
#             response.content
#             )

#     def test_unsuccessful_booking_edit_invalid_end_time(self):
#         """
#         Test for editing an invalid event space booking
#         end time earlier than start time
#         """
#         self.client.login(username="testusername_1", password="testpassword")
#         post_data = {
#             'event_space': self.event_space.id,
#             'occasion': 'test occasion 1',
#             'date': '18/10/2025',
#             'start': '19:00',
#             'end': '17:00',
#             'notes': 'test notes'
#         }
#         response = self.client.post(
#             reverse('booking_edit', args=(self.booking_1.id,)),
#             post_data
#             )

#         # Check error messages are displayed
#         self.assertEqual(response.status_code, 200)
#         self.assertIn(
#             b"Error updating event space booking!",
#             response.content
#             )
#         self.assertIn(
#             b"The end time must be later than the start time.",
#             response.content
#             )

#     def test_unsuccessful_booking_edit_short_duration(self):
#         """
#         Test for editing an invalid event space booking
#         short duration
#         """
#         self.client.login(username="testusername_1", password="testpassword")
#         post_data = {
#             'event_space': self.event_space.id,
#             'occasion': 'test occasion 1',
#             'date': '18/10/2025',
#             'start': '19:00',
#             'end': '19:30',
#             'notes': 'test notes'
#         }
#         response = self.client.post(
#             reverse('booking_edit', args=(self.booking_1.id,)),
#             post_data
#             )

#         # Check error messages are displayed
#         self.assertEqual(response.status_code, 200)
#         self.assertIn(
#             b"Error updating event space booking!",
#             response.content
#             )
#         self.assertIn(
#             b"The end time must be at least 1 hour after the start time.",
#             response.content
#             )

#     def test_unsuccessful_booking_edit_duplicate_booking(self):
#         """
#         Test for editing an invalid event space booking
#         duplicate booking (overlapping with booking_2)
#         """
#         self.client.login(username="testusername_1", password="testpassword")
#         post_data = {
#             'event_space': self.event_space.id,
#             'occasion': 'test occasion 1',
#             'date': '20/10/2025',
#             'start': '17:00',
#             'end': '21:30',
#             'notes': 'test notes'
#         }
#         response = self.client.post(
#             reverse('booking_edit', args=(self.booking_1.id,)),
#             post_data
#             )

#         # Check error messages are displayed
#         self.assertEqual(response.status_code, 200)
#         self.assertIn(
#             b"Error updating event space booking!",
#             response.content
#             )
#         self.assertIn(
#             b"This event space is already booked",
#             response.content
#             )

#     def test_unsuccessful_booking_edit_close_booking(self):
#         """
#         Test for editing an invalid event space booking
#         booking less than 1 hour from booking_2
#         """
#         self.client.login(username="testusername_1", password="testpassword")
#         post_data = {
#             'event_space': self.event_space.id,
#             'occasion': 'test occasion 1',
#             'date': '20/10/2025',
#             'start': '15:00',
#             'end': '18:30',
#             'notes': 'test notes'
#         }
#         response = self.client.post(
#             reverse('booking_edit', args=(self.booking_1.id,)),
#             post_data
#             )

#         # Check error messages are displayed
#         self.assertEqual(response.status_code, 200)
#         self.assertIn(
#             b"Error updating event space booking!",
#             response.content
#             )
#         self.assertIn(
#             b"This event space is already booked",
#             response.content
#             )


# class TestDeleteEventSpaceBookingViews(TestCase):
#     """
#     Test delete event space booking view
#     Test successful and unsuccessful submission
#     Test that user does not have access to other users bookings
#     Test that user does not have access to past bookings
#     """
#     def setUp(self):
#         # Create two Users
#         self.user_1 = User.objects.create_user(
#             username="testusername_1",
#             email="name1@test.com",
#             password="testpassword",
#             is_active=True
#         )

#         self.user_2 = User.objects.create_user(
#             username="testusername_2",
#             email="name2@test.com",
#             password="testpassword",
#             is_active=True
#         )

#         # Create example event space
#         self.event_space = EventSpace.objects.create(
#             name="test space",
#             type="test type",
#             image="test image",
#             building="test building",
#             capacity="10",
#             number_of_tables="10",
#             number_of_chairs="10",
#             kitchen=False,
#             tea_and_coffeemaker=False,
#             projector=False,
#             audio_equipment=False,
#             childrens_play_area=False,
#             piano=False,
#             notes="test notes"
#             )

#         # Create event space bookings, one per user
#         # User 1
#         self.booking_1 = EventSpaceBooking(
#             resident=self.user_1,
#             event_space=self.event_space,
#             occasion="test occasion 1",
#             date="2025-10-18",
#             start=datetime.datetime.strptime('19:00', '%H:%M').time(),
#             end=datetime.datetime.strptime('22:00', '%H:%M').time(),
#             notes="test notes",
#             created_on=datetime.datetime.today(),
#             status="0"
#             )
#         self.booking_1.save()

#         # User 2
#         self.booking_2 = EventSpaceBooking(
#             resident=self.user_2,
#             event_space=self.event_space,
#             occasion="test occasion 2",
#             date="2025-10-20",
#             start=datetime.datetime.strptime('19:00', '%H:%M').time(),
#             end=datetime.datetime.strptime('22:00', '%H:%M').time(),
#             notes="test notes",
#             created_on=datetime.datetime.today(),
#             status="0"
#             )
#         self.booking_2.save()

#         # Past Booking from User 1
#         self.booking_3 = EventSpaceBooking(
#             resident=self.user_1,
#             event_space=self.event_space,
#             occasion="test occasion 3",
#             date="2024-10-20",
#             start=datetime.datetime.strptime('19:00', '%H:%M').time(),
#             end=datetime.datetime.strptime('22:00', '%H:%M').time(),
#             notes="test notes",
#             created_on=datetime.datetime.today(),
#             status="0"
#             )
#         self.booking_3.save()

#     def test_no_access_unauthenticated_user(self):
#         """
#         Verifies that unauthenticated users don't have access to bookings
#         """
#         # Send GET request and store response
#         response = self.client.get(
#             reverse('booking_delete', args=(self.booking_1.id,))
#             )
#         # Redirects correctly
#         self.assertEqual(response.status_code, 302)
#         self.assertRedirects(
#             response,
#             '/accounts/login/?next=/dashboard/delete_booking/1'
#             )

#     def test_no_access_for_wrong_booking(self):
#         """
#         Verifies that user cannot delete bookings from other users
#         """
#         # note specifiy which user!
#         self.client.login(username="testusername_1", password="testpassword")
#         # Send GET request and store response
#         response = self.client.get(
#             # booking_2 is booking from other user
#             reverse('booking_delete', args=(self.booking_2.id,)),
#             follow=True
#             )
#         # Check message
#         self.assertEqual(response.status_code, 200)
#         self.assertIn(
#             b"You do not have access to this booking.",
#             response.content
#         )

#     def test_no_access_for_past_booking(self):
#         """
#         Verifies that user cannot delete past bookings
#         """
#         # note specifiy which user!
#         self.client.login(username="testusername_1", password="testpassword")
#         # Send GET request and store response
#         response = self.client.get(
#             # booking_3 is booking in past from this user
#             reverse('booking_delete', args=(self.booking_3.id,)),
#             follow=True
#             )
#         # Check message
#         self.assertEqual(response.status_code, 200)
#         self.assertIn(
#             b"You cannot delete past bookings.",
#             response.content
#         )

#     def test_successful_delete_booking(self):
#         """
#         Verifies that user successfully delete booking
#         """
#         # note specifiy which user!
#         self.client.login(username="testusername_1", password="testpassword")
#         # Send GET request and store response
#         response = self.client.get(
#             reverse('booking_delete', args=(self.booking_1.id,)),
#             follow=True
#             )
#         # Check message
#         self.assertEqual(response.status_code, 200)
#         self.assertIn(
#             b"Event Space Booking successfully deleted!",
#             response.content
#         )


# class TestEventSpacesListView(TestCase):
#     """
#     Test event spaces list view
#     Test that content rendered correctly
#     """
#     def setUp(self):
#         # Create User
#         self.user = User.objects.create_user(
#             username="testusername",
#             email="name1@test.com",
#             password="testpassword",
#             is_active=True
#         )

#         # Create example event spaces
#         self.event_space_1 = EventSpace.objects.create(
#             name="test space 1",
#             type="test type 1",
#             image="test image",
#             building="test building 1",
#             capacity="10",
#             number_of_tables="10",
#             number_of_chairs="10",
#             kitchen=False,
#             tea_and_coffeemaker=False,
#             projector=False,
#             audio_equipment=False,
#             childrens_play_area=False,
#             piano=False,
#             notes="test notes"
#             )

#         self.event_space_2 = EventSpace.objects.create(
#             name="test space 2",
#             type="test type 2",
#             image="test image",
#             building="test building 2",
#             capacity="10",
#             number_of_tables="10",
#             number_of_chairs="10",
#             kitchen=False,
#             tea_and_coffeemaker=False,
#             projector=False,
#             audio_equipment=False,
#             childrens_play_area=False,
#             piano=False,
#             notes="test notes"
#             )

#     def test_render_content_for_authenticated_users(self):
#         self.client.login(username="testusername", password="testpassword")
#         response = self.client.get(reverse('event_spaces'))
#         # Page is rendered correctly
#         self.assertEqual(response.status_code, 200)
#         # Check content for logged in users
#         self.assertIn(b"Event Spaces", response.content)

#         # Check that event spaces are displayed (check several fields)
#         self.assertIn(b"test space 1", response.content)
#         self.assertIn(b"test type 1", response.content)
#         self.assertIn(b"test building 1", response.content)
#         self.assertIn(b"test space 2", response.content)
#         self.assertIn(b"test type 2", response.content)
#         self.assertIn(b"test building 2", response.content)
#         self.assertIn(b"Book this Space", response.content)

#     def test_render_content_for_unauthenticated_users(self):
#         response = self.client.get(reverse('event_spaces'))
#         # Check redirect
#         self.assertEqual(response.status_code, 302)
#         self.assertRedirects(
#             response,
#             '/accounts/login/?next=/dashboard/event_spaces/'
#             )


# class TestResidentRequestSubmissionView(TestCase):
#     """
#     Test resident request view
#     Render page with request submission form
#     Test successful and unsuccessful submission
#     """
#     def setUp(self):
#         # Create User
#         self.user = User.objects.create_user(
#             username="testusername",
#             email="name@test.com",
#             password="testpassword",
#             is_active=True
#         )

#     def test_not_render_submission_page_unauthenticated_user(self):
#         """
#         Verifies that unauthenticated users don't have access to
#         request submission page
#         """
#         # Send GET request and store response
#         response = self.client.get(reverse('resident_request'))
#         # Redirects correctly
#         self.assertEqual(response.status_code, 302)
#         self.assertRedirects(
#             response,
#             '/accounts/login/?next=/dashboard/submit_request/'
#             )

#     def test_render_submission_page_with_resident_request_form(self):
#         """
#         Verifies get request for resident request submission page containing a
#         booking form
#         """
#         self.client.login(username="testusername", password="testpassword")
#         # Send GET request and store response
#         response = self.client.get(reverse('resident_request'))
#         # Page is rendered correctly
#         self.assertEqual(response.status_code, 200)
#         # The context is instance of correct form
#         self.assertIsInstance(
#             response.context['resident_request_form'],
#             ResidentRequestForm
#             )

#     def test_successful_maintenance_request_submission(self):
#         """Test for submitting a maintenance request"""
#         self.client.login(username="testusername", password="testpassword")
#         post_data = {
#             'purpose': '0',
#             'urgent': True,
#             'content': 'test maintenance request',
#         }
#         response = self.client.post(
#             reverse('resident_request'),
#             post_data,
#             follow=True
#             )

#         # Check content on dashboard and messages
#         self.assertEqual(response.status_code, 200)
#         self.assertIn(b"Maintenance Request", response.content)
#         self.assertIn(b"Urgent!", response.content)
#         self.assertIn(b"test maintenance request", response.content)
#         # Success message
#         self.assertIn(
#             b"You successfully sent a maintenance request.",
#             response.content
#             )

#     def test_successful_message_submission(self):
#         """Test for submitting a message"""
#         self.client.login(username="testusername", password="testpassword")
#         post_data = {
#             'purpose': '1',
#             'urgent': False,
#             'content': 'test message',
#         }
#         response = self.client.post(
#             reverse('resident_request'),
#             post_data,
#             follow=True
#             )

#         # Check content on dashboard and messages
#         self.assertEqual(response.status_code, 200)
#         self.assertIn(b"Message", response.content)
#         # not urgent
#         self.assertNotIn(b"Urgent!", response.content)
#         self.assertIn(b"test message", response.content)
#         # Success message
#         self.assertIn(
#             b"You successfully sent a message.",
#             response.content
#             )

#     def test_unsuccessful_request_submission_invalid_purpose(self):
#         """
#         Test for submitting an invalid resident request
#         invalid purpose
#         """
#         self.client.login(username="testusername", password="testpassword")
#         post_data = {
#             'purpose': 'purpose',
#             'urgent': True,
#             'content': 'test maintenance request',
#         }
#         response = self.client.post(reverse('resident_request'), post_data)

#         # Check that stay on page and error message displayed
#         self.assertEqual(response.status_code, 200)
#         self.assertIn(
#             b"There was an error in your form.",
#             response.content
#             )


# class TestEditResidentRequestView(TestCase):
#     """
#     Test edit resident request view
#     Render page with prefilled submission form
#     Test successful and unsuccessful submission
#     Test that user does not have access to other users requests
#     """
#     def setUp(self):
#         # Create two Users
#         self.user_1 = User.objects.create_user(
#             username="testusername_1",
#             email="name1@test.com",
#             password="testpassword",
#             is_active=True
#         )

#         self.user_2 = User.objects.create_user(
#             username="testusername_2",
#             email="name2@test.com",
#             password="testpassword",
#             is_active=True
#         )

#         # Create resident requests, one per user
#         # maint request from user 1
#         self.res_request_1 = ResidentRequest(
#             resident=self.user_1,
#             purpose="0",
#             urgent=True,
#             content="test maintenance request 1",
#             created_on=datetime.datetime.today(),
#             status="0"
#             )
#         self.res_request_1.save()

#         # message from user 2
#         self.res_request_2 = ResidentRequest(
#             resident=self.user_2,
#             purpose="1",
#             urgent=False,
#             content="test message 2",
#             created_on=datetime.datetime.today(),
#             status="1"
#             )
#         self.res_request_2.save()

#     def test_not_render_edit_request_page_unauthenticated_user(self):
#         """
#         Verifies that unauthenticated users don't have access to edit
#         resident requests page
#         """
#         # Send GET request and store response
#         response = self.client.get(
#             reverse('resident_request_edit', args=(self.res_request_1.id,))
#             )
#         # Redirects correctly
#         self.assertEqual(response.status_code, 302)
#         self.assertRedirects(
#             response,
#             '/accounts/login/?next=/dashboard/edit_resident_request/1'
#             )

#     def test_not_render_edit_request_page_wrong_user(self):
#         """
#         Verifies that users don't have access to edit
#         resident requests from other users
#         """
#         self.client.login(username="testusername_1", password="testpassword")
#         # Send GET request and store response
#         # res_request_2 is from other user
#         response = self.client.get(
#             reverse('resident_request_edit', args=(self.res_request_2.id,))
#             )
#         # Redirects correctly
#         self.assertEqual(response.status_code, 302)
#         self.assertRedirects(response, reverse('dashboard'))

#     def test_render_submission_page_with_edit_resident_form(self):
#         """
#         Verifies get request for edit resident request page containing a
#         resident request submission form which is prefilled
#         """
#         # note specifiy which user!
#         self.client.login(username="testusername_1", password="testpassword")
#         # Send GET request and store response
#         response = self.client.get(
#             reverse('resident_request_edit', args=(self.res_request_1.id,))
#             )
#         # Page is rendered correctly
#         self.assertEqual(response.status_code, 200)
#         # The context is instance of correct form
#         self.assertIsInstance(
#             response.context['resident_request_form'],
#             ResidentRequestForm
#             )
#         # Check that form is prefilled
#         self.assertIn(b"maintenance request", response.content)
#         self.assertIn(b"test maintenance request 1", response.content)

#     def test_successful_resident_request_edit(self):
#         """Test for editing a resident request (change content and urgent)"""
#         self.client.login(username="testusername_1", password="testpassword")
#         post_data = {
#             'purpose': '0',
#             'urgent': False,
#             'content': 'test edit request'
#         }
#         response = self.client.post(
#             reverse('resident_request_edit', args=(self.res_request_1.id,)),
#             post_data,
#             follow=True
#             )

#         # Check content of dashboard (focus on messages)
#         self.assertEqual(response.status_code, 200)
#         # check success message
#         self.assertIn(
#             b"You successfully updated your maintenance request",
#             response.content
#             )
#         # check updated content
#         self.assertIn(b"test edit request", response.content)

#     def test_resident_request_not_changed(self):
#         """Test for editing a resident request with no change"""
#         # Note check for user 2 here
#         self.client.login(username="testusername_2", password="testpassword")
#         post_data = {
#             'purpose': '1',
#             'urgent': False,
#             'content': 'test message 2'
#         }
#         # With follow=True follows the redirect and can check content of the
#         # page that is redirected to
#         response = self.client.post(
#             reverse('resident_request_edit', args=(self.res_request_2.id,)),
#             post_data,
#             follow=True
#             )

#         # Check content of dashboard (focus on messages)
#         self.assertEqual(response.status_code, 200)
#         self.assertIn(
#             b"No changes were made to your message.",
#             response.content
#             )


# class TestDeleteResidentRequestView(TestCase):
#     """
#     Test delete resident request view
#     Test successful and unsuccessful submission
#     Test that user does not have access to other users requests
#     """
#     def setUp(self):
#         # Create two Users
#         self.user_1 = User.objects.create_user(
#             username="testusername_1",
#             email="name1@test.com",
#             password="testpassword",
#             is_active=True
#         )

#         self.user_2 = User.objects.create_user(
#             username="testusername_2",
#             email="name2@test.com",
#             password="testpassword",
#             is_active=True
#         )

#         # Create resident requests, one per user
#         # maint request from user 1
#         self.res_request_1 = ResidentRequest(
#             resident=self.user_1,
#             purpose="0",
#             urgent=True,
#             content="test maintenance request 1",
#             created_on=datetime.datetime.today(),
#             status="0"
#             )
#         self.res_request_1.save()

#         # message from user 2
#         self.res_request_2 = ResidentRequest(
#             resident=self.user_2,
#             purpose="1",
#             urgent=False,
#             content="test message 2",
#             created_on=datetime.datetime.today(),
#             status="1"
#             )
#         self.res_request_2.save()

#     def test_no_access_unauthenticated_user(self):
#         """
#         Verifies that unauthenticated users don't have access to requests
#         """
#         # Send GET request and store response
#         response = self.client.get(
#             reverse('resident_request_delete', args=(self.res_request_1.id,))
#             )
#         # Redirects correctly
#         self.assertEqual(response.status_code, 302)
#         self.assertRedirects(
#             response,
#             '/accounts/login/?next=/dashboard/delete_resident_request/1'
#             )

#     def test_no_access_for_wrong_request(self):
#         """
#         Verifies that user cannot delete requests from other users
#         """
#         # note specifiy which user!
#         self.client.login(username="testusername_1", password="testpassword")
#         # Send GET request and store response
#         response = self.client.get(
#             # res_request_2 is message from other user
#             reverse('resident_request_delete', args=(self.res_request_2.id,)),
#             follow=True
#             )
#         # Check message
#         self.assertEqual(response.status_code, 200)
#         self.assertIn(
#             b"You do not have access to this message.",
#             response.content
#         )

#     def test_successful_delete_request(self):
#         """
#         Verifies that user successfully delete resident request
#         """
#         # note specifiy which user!
#         self.client.login(username="testusername_1", password="testpassword")
#         # Send GET request and store response
#         response = self.client.get(
#             reverse('resident_request_delete', args=(self.res_request_1.id,)),
#             follow=True
#             )
#         # Check message
#         self.assertEqual(response.status_code, 200)
#         self.assertIn(
#             b"Maintenance request successfully deleted!",
#             response.content
#         )
