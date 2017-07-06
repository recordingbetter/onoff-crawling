from django import forms

class SearchForm(forms.Form):
    q_search = forms.CharField(
        max_length=64,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Search...',
            }
        )
    )