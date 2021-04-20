from django import forms
from .models import Review

class ReviewForm(forms.Form):
    contents = forms.CharField(max_length=100)
    
    class Meta:
        model = Review

class DelReviewForm(forms.Form):
    deleteid = forms.CharField(max_length=100)
    
class EditReviewForm(forms.Form):
    reviewid = forms.CharField(max_length=100)
    changecontents = forms.CharField(max_length=100)