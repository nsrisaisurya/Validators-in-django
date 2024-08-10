from app.models import *

from django import forms

def check_for_a(subvalue):
    if subvalue[0]=='a':
        raise forms.ValidationError('name startswith a')


def check_for_len(subvalue):
    if len(subvalue)<5:
        raise forms.ValidationError('length should be min 5')




    





class WebpageForm(forms.Form):
    topicname=forms.ModelChoiceField(queryset=Topic.objects.all())
    name=forms.CharField(max_length=100,validators=[check_for_a,check_for_len])
    url=forms.URLField()
    
