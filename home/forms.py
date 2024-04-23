from django import forms

class DatasetUploadForm(forms.Form):
    dataset = forms.FileField(label='Upload Dataset' ,widget=forms.FileInput(attrs={'accept': '.csv'}))

