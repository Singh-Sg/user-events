from django import forms
from .models import Event


class EventForm(forms.ModelForm):

    class Meta:
        model = Event
        fields = ('title', 'description')

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(EventForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        obj = super(EventForm, self).save(commit=False)
        if self.user:
            obj.user = self.user
        if commit:
            obj.save()
        return obj
