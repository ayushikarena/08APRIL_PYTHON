from django import forms
from .models import UserProfile

class UserProfileForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        fields = '__all__'

    def clean_age(self):
        age = self.cleaned_data.get('age')

        if age < 13:
            raise forms.ValidationError("User must be at least 13 years old.")

        return age