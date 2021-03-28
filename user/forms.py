from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(label = "Username")
    password = forms.CharField(label = "password",widget = forms.PasswordInput)


class RegisterForm(forms.Form):
    username = forms.CharField(max_length = 50,label = "Username")
    password = forms.CharField(max_length=20,label = "password",widget = forms.PasswordInput)
    confirm = forms.CharField(max_length=20,label ="password again",widget = forms.PasswordInput)
    
    def clean(self):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        confirm = self.cleaned_data.get("confirm")

        if password and confirm and password != confirm:
            raise forms.ValidationError("password is not much")

        values = {
            "username" : username,
            "password" : password
        }
        return values


