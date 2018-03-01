from django import forms

from .models import Comments,BlogPost

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comments
        fields = ('comment',)


class BlogForm(forms.ModelForm):

    class Meta:
        model = BlogPost
        fields = ('title',
                  'contentText')