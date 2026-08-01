from django import forms
from .models import Profile

class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = "__all__"

    def clean_age(self):
        age = self.cleaned_data.get("age")

        if age < 13:
            raise forms.ValidationError("Age must be at least 13.")

        return age