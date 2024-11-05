from django import forms

from app.models import Study


class Studyform(forms.ModelForm):
    sponsor_name = forms.CharField(
        max_length=100,
        label="Sponsor Name",
        widget=forms.TextInput(attrs={'list': 'sponsor_list'})
    )

    class Meta:
        model = Study
        fields = "__all__"
