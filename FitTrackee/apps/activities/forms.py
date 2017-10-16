from django import forms

from .models import Sport, Gpx, Comment


def validate_file_extension(value):
    import os
    from django.core.exceptions import ValidationError
    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    valid_extensions = ['.gpx']
    if not ext.lower() in valid_extensions:
        raise ValidationError(u'Unsupported file extension. Only *.gpx')


class AddActivityForm(forms.Form):
    sport = forms.ModelChoiceField(queryset=Sport.objects.all(), required=True)
    gpx_file = forms.FileField(required=True, validators=[validate_file_extension])

    class Meta:
        model = Gpx
        fields = ('gpx_file', )


class AddCommentForm(forms.Form):
    comment = forms.CharField(widget=forms.Textarea(attrs={'rows': '4'}))

    class Meta:
        model = Comment
        fields = ('comment', )
