from django import forms


class SearchFrom(forms.Form):
    keyword = forms.CharField(label='', max_length=255, required=True,
                              widget=forms.TextInput(attrs={
                                  'class': 'search-keyword',
                              }))
