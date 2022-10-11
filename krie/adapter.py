from allauth.account.adapter import DefaultAccountAdapter
from django.forms import ValidationError


class UsernameMaxAdapter(DefaultAccountAdapter):
    """
    Set the max length of a username to 15
    """

    def clean_username(self, username):
        if len(username) > 15:
            raise ValidationError(
                'A username must be a maximum of 15 characters.')
        return DefaultAccountAdapter.clean_username(self, username)
