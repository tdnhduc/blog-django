from django import forms

class Subscribe(forms.Form):
    email = forms.EmailField()

    def __str__(self):
        return self.email


class Search(forms.Form):
    search = forms.CharField(label='search',max_length=100)

    def __str__(self):
        return self.search