from django import forms

from .models import UserComments

# ADD COMMENT FORM CLASS
class CommentForm(forms.ModelForm):
  class Meta:
    model = UserComments