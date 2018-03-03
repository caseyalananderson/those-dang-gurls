from django import forms


# Users can add comments
class CommentForm(forms.Form):
    """
    Form that holds the User Comments for the Food Entries
    """
    content_type = forms.CharField(widget=forms.HiddenInput)
    object_id = forms.IntegerField(widget=forms.HiddenInput)
    # parent_id = forms.IntegerField(widget=forms.HiddenInput)
    content = forms.CharField(widget=forms.Textarea)



