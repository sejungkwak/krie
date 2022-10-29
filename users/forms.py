from django import forms
from django.contrib.auth.models import User
from .models import Profile
from crispy_forms.helper import FormHelper

choice_list = [
    ('', 'Choose your county'),
    ('Antrim', 'Antrim'),
    ('Armagh', 'Armagh'),
    ('Carlow', 'Carlow'),
    ('Cavan', 'Cavan'),
    ('Clare', 'Clare'),
    ('Cork', 'Cork'),
    ('Donegal', 'Donegal'),
    ('Down', 'Down'),
    ('Dublin', 'Dublin'),
    ('Fermanagh', 'Fermanagh'),
    ('Galway', 'Galway'),
    ('Kerry', 'Kerry'),
    ('Kildare', 'Kildare'),
    ('Kilkenny', 'Kilkenny'),
    ('Laois', 'Laois'),
    ('Leitrim', 'Leitrim'),
    ('Limerick', 'Limerick'),
    ('Londonderry', 'Londonderry'),
    ('Longford', 'Longford'),
    ('Louth', 'Louth'),
    ('Mayo', 'Mayo'),
    ('Meath', 'Meath'),
    ('Monaghan', 'Monaghan'),
    ('Offaly', 'Offaly'),
    ('Roscommon', 'Roscommon'),
    ('Sligo', 'Sligo'),
    ('Tipperary', 'Tipperary'),
    ('Tyrone', 'Tyrone'),
    ('Waterford', 'Waterford'),
    ('Westmeath', 'Westmeath'),
    ('Wexford', 'Wexford'),
    ('Wicklow', 'Wicklow')
]


class UserUpdateForm(forms.ModelForm):
    """
    Represent a form for updating the user data
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(form=self)
        self.fields['username'].widget.attrs.update({'maxlength': 15})
        self.fields['username'].help_text = ('15 characters or fewer. Letters,'
                                             ' digits and @/./+/-/_ only.')

    class Meta:
        model = User
        fields = ['username', 'email']
        widgets = {
            'username': forms.TextInput(),
            'email': forms.EmailInput()}

    def clean(self):
        """
        Check if the email address is already in use.
        """
        super().clean()
        email = self.cleaned_data.get('email')

        if email and User.objects.filter(email=email).count() > 1:
            raise forms.ValidationError(f'{email} is already in use.')
        return self.cleaned_data


class ProfileUpdateForm(forms.ModelForm):
    """
    Represent a form for updating the profile data
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(form=self)
        self.fields['bio'].label = 'About yourself'

    class Meta:
        model = Profile
        fields = ['location', 'bio']
        widgets = {
            'location': forms.Select(
                choices=choice_list,
                attrs={
                    'class': 'form-select'}),
            'bio': forms.Textarea()}
