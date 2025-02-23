from django import forms
from dashboard.models import EventSpace


class EventSpaceForm(forms.ModelForm):
    """
    Form for creating event spaces (for admins only)
    Based on the EventSpace model

    Fields:
        - name (CharField)
        - type (CharField)
        - image (CloudinaryField, optional)
        - building (CharField)
        - capacity (IntegerField)
        - number_of_tables (IntegerField)
        - number_of_chairs (IntegerField)
        - kitchen (BooleanField)
        - tea_and_coffeemaker (BooleanField)
        - projector (BooleanField)
        - audio_equipment (BooleanField)
        - childrens_play_area (BooleanField)
        - piano (BooleanField)
        - notes (TextField, optional)
    """
    class Meta:
        model = EventSpace
        fields = (
            'name',
            'type',
            'image',
            'building',
            'capacity',
            'number_of_tables',
            'number_of_chairs',
            'kitchen',
            'tea_and_coffeemaker',
            'projector',
            'audio_equipment',
            'childrens_play_area',
            'piano',
            'notes',
            )
        # Removes the "Currently" field when editing
        # Code inspiration from: https://stackoverflow.com/a/6076245
        widgets = {
            'image': forms.FileInput(),
        }
