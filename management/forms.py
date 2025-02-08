from django import forms
from dashboard.models import EventSpace


class EventSpaceForm(forms.ModelForm):
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
            'tea_and_coffemaker',
            'projector',
            'audio_equipment',
            'childrens_play_area',
            'piano',
            'notes',
            )
