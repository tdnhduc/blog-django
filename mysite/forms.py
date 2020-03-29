from django import forms

class Subscribe(forms.Form):
    email = forms.EmailField()

    def __str__(self):
        return self.email