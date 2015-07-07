# -*- coding: utf-8 -*-
from django import forms

class ImageForm(forms.Form):
    file = forms.FileField(
        label="Select a file")
    description = forms.CharField(max_length=100,
        label="Description",
        required=False)