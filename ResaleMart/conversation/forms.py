from django import forms as fr

from .models import conversationMessage

class conversationmessageform( fr.ModelForm ):
    class Meta:
        model = conversationMessage
        fields = ('content',)
        widgets = {
            'content': fr.Textarea(attrs = {
                'class': 'w-full py-4 px-6 rounded-xl boder'
            })
        }