from django import forms
from ghostPost.models import BoastnRoast


# class BoastorRoast(forms.Form):
#     boast_or_roast = forms.BooleanField()
#     message = forms.CharField(max_length=280)


class BoastorRoast(forms.ModelForm):
    class Meta:
        model = BoastnRoast
        fields = ['boast', 'message', ]
