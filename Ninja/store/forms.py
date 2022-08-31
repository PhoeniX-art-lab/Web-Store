from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class PlaceholderForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(PlaceholderForm, self).__init__(*args, **kwargs)
        for _, field in self.fields.items():
            field.widget.attrs['placeholder'] = field.help_text


class SupportForm(PlaceholderForm):
    email = forms.EmailField(
        help_text='Your email'
    )
    choices1 = [('Product and Technical Support', 'Product and Technical Support'),
                ('Service Plans', 'Service Plans'),
                ('Dji Store Order Inquiry', 'Dji Store Order Inquiry'),
                ('Repair or Replacement Progress', 'Repair or Replacement Progress')]
    issue_type = forms.ChoiceField(widget=forms.Select(attrs={'class': 'select-form'}), choices=choices1)
    text = forms.CharField(
        widget=forms.Textarea(attrs={'cols': 30, 'rows': 10}),
        label='Description of needs', help_text='Please give a description of your demand or problem'
    )


class UserRegistrationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')


class LoginForm(AuthenticationForm):
    pass
