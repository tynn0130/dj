from django import forms
from django.utils.translation import gettext_lazy as _

class LogInputForm(forms.Form):
    log_text = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 10, 'placeholder': _('Paste your log here...')}),
        required=False,
        label=_('Log Text')
    )
    log_file = forms.FileField(
        widget=forms.ClearableFileInput(attrs={'class': 'form-control'}),
        required=False,
        label=_('Upload Log File')
    )

    def clean(self):
        cleaned_data = super().clean()
        log_text = cleaned_data.get("log_text")
        log_file = cleaned_data.get("log_file")

        if not log_text and not log_file:
            raise forms.ValidationError(_("Please provide either log text or upload a log file."))
        
        return cleaned_data
