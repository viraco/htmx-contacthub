from django import forms

from contacts.models import Contact


class ContactForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(
                            attrs={'class': 'input input-bordered w-full',
                                   'placeholder': 'Contact Name'}))
    email = forms.EmailField(widget=forms.EmailInput(
                            attrs={'class': 'input input-bordered w-full',
                                   'placeholder': 'Contact Email'}))

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if Contact.objects.filter(user = self.initial.get('user'), email=email).exists():
            raise forms.ValidationError('This email is already in use.')
        return email

    class Meta:
        model = Contact
        fields = ['name', 'email']