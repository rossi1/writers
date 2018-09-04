from django.contrib.auth.forms  import UserCreationForm
from django.contrib.auth import get_user_model



class SignupForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ['email']

    def signup(self, request, user):
        user.is_user = True
        user.save()
