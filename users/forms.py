from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class customUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name','email', 'password1', 'password2' ]
        label = {
            'first_name':'Name'
        }

    
    def __init__(self, *args, **kwargs):
        super(customUserCreationForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'input'})
        # self.fields['title'].widget.attrs.update({'class':'input'} )