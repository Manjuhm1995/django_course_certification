from django import forms
from . models import Review


# class ReviewForm(forms.Form):
#     user_name = forms.CharField(label="Your Name", max_length=100, error_messages={
#         "required": "Your name must not be empty!",
#         "max_length": "Please enter a shorter name!"
#     })
#     review_text=forms.CharField(label="Your Feedback", widget=forms.Textarea,max_length=200)
#     rating=forms.IntegerField(label="Your Rating",min_value=1,max_value=5)
class ReviewForm(forms.ModelForm):
    class Meta:
        model=Review
        fields="__all__"# to apply all the fields in model are part of the form
        # exclude=[" ", " ", " "]# except some fields to apply all the fields in model are part of the form
        # fields=[" ", " ", " "]# to have necessary fields in the model are the part of the form
        labels={"user_name":"Your Name","review_text":"Your Feedback","Your Rating":"rating"}
        error_messages={"user_name":{
            "required": "Your name must not be empty!",
            "max_length": "Please enter a shorter name!"
            }}
        # IntegerField={"min_value":1,"max_value":5}
        IntegerField={"rating":{"min_value":1}}

