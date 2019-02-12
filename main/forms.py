from django import forms


class FeedbackForm(forms.Form):
    nickname = forms.CharField(max_length=30, label='', widget=forms.TextInput({"placeholder": "Псевдоним"}))
    email = forms.EmailField(max_length=245, label='', widget=forms.TextInput({"placeholder": "Адрес электронной почты"}))
    subject = forms.CharField(max_length=50, label='', widget=forms.TextInput({"placeholder": "Тема"}))
    text = forms.CharField(label='', widget=forms.Textarea)

