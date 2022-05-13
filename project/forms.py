from django.forms import ModelForm
from .models import Project
from django import forms


class AddProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['title','featured_image', 'descriptions', 'tag', 'demo_link', 'source_link']

        widgets = {
            'tag': forms.CheckboxSelectMultiple(),
        }

    def __init__(self, *args, **kwargs):
        super(AddProjectForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'input'})
        # self.fields['title'].widget.attrs.update({'class':'input'} )