from django import forms
'''The below class defines a search bar form for search functionality'''

class SearchBar(forms.Form):
    Search = forms.CharField(max_length=100)