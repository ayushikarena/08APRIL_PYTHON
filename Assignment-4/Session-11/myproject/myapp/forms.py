from django import forms
from .models import InfluencerProfile

class ProfileForm(forms.ModelForm):

    class Meta:

        model = InfluencerProfile

        fields = [
            'display_name',
            'bio',
            'profile_pic',
            'phone_number'
        ]