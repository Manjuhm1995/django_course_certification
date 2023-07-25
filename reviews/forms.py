from django import forms
class ReviewForm(forms.Form):
    user_name=forms.CharField(label="Your Name",max_length=10,error_messages={
        "required":"Your Name should not be empty",
        "max_length":" Your Name should be shorter"
    })




