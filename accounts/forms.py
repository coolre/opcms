from django import forms

# from pagedown.widgets import PagedownWidget

from .models import Opuser


class RegisterForm(forms.Form):
    username = forms.CharField()
    identification = forms.CharField()
    mobile = forms.CharField()
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        if len(password1) <= 4:
            raise forms.ValidationError("Password is too short")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def clean_username(self):
        username = self.cleaned_data.get("username")

        username_qs = Opuser.objects.filter(username=username)
        if username_qs.exists():
            raise forms.ValidationError("This email has already been registered")
        return username
        # try:
        #     exists = Opuser.objects.get(username=username)
        #     raise forms.ValidationError("This username is taken")
        # except Opuser.DoesNotExist:
        #     return username
        # except:
        #     raise forms.ValidationError("There was an error, please try again or contact us.")

    #
    def clean_identification(self):
        identification = self.cleaned_data.get("identification")
        identification_qs = Opuser.objects.filter(identification=identification)
        if identification_qs.exists():
            raise forms.ValidationError("This identification has already been registered")
        return identification


    def clean_mobile(self):
        mobile = self.cleaned_data.get("mobile")
        mobile_qs = Opuser.objects.filter(mobile=mobile)
        if mobile_qs.exists():
            raise forms.ValidationError("This mobile has already been registered")
        return mobile