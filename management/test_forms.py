from django.test import TestCase
from .forms import EventSpaceForm


class TestEventSpaceForm(TestCase):
    """
    Test Event Space Form (in Admin Space)
    """
    def test_form_is_valid(self):
        event_space_form = EventSpaceForm({
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
            })
        self.assertTrue(event_space_form.is_valid(), msg="Form is invalid")

    # check that image is optional
    def test_form_is_valid_with_no_image(self):
        event_space_form = EventSpaceForm({
            'name': 'test name',
            'type': 'test name',
            'image': '',
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
            })
        self.assertTrue(
            event_space_form.is_valid(),
            msg="No image and form is invalid"
            )

    # check that notes are optional
    def test_form_is_valid_with_no_notes(self):
        event_space_form = EventSpaceForm({
            'name': 'test name',
            'type': 'test name',
            'image': 'test image',
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
            'notes': '',
            })
        self.assertTrue(
            event_space_form.is_valid(),
            msg="No notes and form is invalid"
            )

    # check that form invalid with missing fields
    def test_form_is_invalid_missing_name(self):
        event_space_form = EventSpaceForm({
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
            })
        self.assertFalse(
            event_space_form.is_valid(),
            msg="No name provided, but form is invalid")

    def test_form_is_invalid_missing_type(self):
        event_space_form = EventSpaceForm({
            'name': 'test name',
            'type': '',
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
            })
        self.assertFalse(
            event_space_form.is_valid(),
            msg="No type provided, but form is invalid")

    def test_form_is_invalid_missing_building(self):
        event_space_form = EventSpaceForm({
            'name': 'test name',
            'type': 'test name',
            'image': 'test name',
            'building': '',
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
            })
        self.assertFalse(
            event_space_form.is_valid(),
            msg="No building provided, but form is invalid")

    def test_form_is_invalid_missing_capacity(self):
        event_space_form = EventSpaceForm({
            'name': 'test name',
            'type': 'test name',
            'image': 'test name',
            'building': 'test name',
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
            })
        self.assertFalse(
            event_space_form.is_valid(),
            msg="No capacity provided, but form is invalid")

    def test_form_is_invalid_missing_number_tables(self):
        event_space_form = EventSpaceForm({
            'name': 'test name',
            'type': 'test name',
            'image': 'test name',
            'building': 'test name',
            'capacity': '10',
            'number_of_tables': '',
            'number_of_chairs': '10',
            'kitchen': True,
            'tea_and_coffeemaker': True,
            'projector': True,
            'audio_equipment': True,
            'childrens_play_area': True,
            'piano': True,
            'notes': 'test notes',
            })
        self.assertFalse(
            event_space_form.is_valid(),
            msg="No number of tables provided, but form is invalid")

    def test_form_is_invalid_missing_number_chairs(self):
        event_space_form = EventSpaceForm({
            'name': 'test name',
            'type': 'test name',
            'image': 'test name',
            'building': 'test name',
            'capacity': '10',
            'number_of_tables': '10',
            'number_of_chairs': '',
            'kitchen': True,
            'tea_and_coffeemaker': True,
            'projector': True,
            'audio_equipment': True,
            'childrens_play_area': True,
            'piano': True,
            'notes': 'test notes',
            })
        self.assertFalse(
            event_space_form.is_valid(),
            msg="No number of chairs provided, but form is invalid")
