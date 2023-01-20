#-*- coding: utf-8 -*-
from django import forms

class answer(forms.Form):
    ans_opt_sol = forms.CharField(max_length = 200,required=False)

class uploaded_file(forms.Form):
    file = forms.FileField()
