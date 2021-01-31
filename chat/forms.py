from django import forms

class MessageForm(forms.Form):
    message = forms.CharField( widget=forms.TextInput(attrs={"id":"message-to-send","placeholder":"Your message:"}))
    conversation = forms.HiddenInput()