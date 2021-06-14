from django import forms

from .models import userinfo

class TransferForm(forms.Form):
    sender_name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(
            attrs={'class':'form-control', 'readonly':True}
        ),
        label='From:'
    )
    reciever_name = forms.ChoiceField(
        choices=userinfo.objects.values_list('id', 'name'),
    )
    # reciever_name = forms.CharField(
    #     max_length=100,
    #     widget=forms.TextInput(
    #         attrs={'class':'form-control'}
    #     ),
    #     label='To:'
    # )
    amount = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={'class':'form-control', 'onkeyup':'check()'}
        ),
        label='Amount:'
    )

    reciever_name.widget.attrs.update({'class':'form-control'})