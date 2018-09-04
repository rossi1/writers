from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

from .models import WritersProfile

class WriterSignupForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        exclude = ('is_writer', 'is_user')

    def save(self, commit=True):
        instance = super(WriterSignupForm, self).save(commit=False)
        if not instance.is_writer:
            instance.is_writer = True
            if commit:
                instance.save()
            return instance

class WriterProfileForm(forms.ModelForm):
    class Meta:
        model = WritersProfile
        fields = '__all__'
