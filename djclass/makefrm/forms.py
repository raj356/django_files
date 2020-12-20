from django import forms
from makefrm.models import Teacher

class TeachForm(forms.ModelForm):
    class Meta:
        model=Teacher
        fields=[
            'name',
            'age',
            'gender',
            'pic',
            'sub'
        ]
        labels={
            'name':'NAME',
            'age':'AGE',
            'gender':'GENDER',
            'pic':'PICTURE',
            'sub':'SUBJECT'
        }

    def __init__(self, *args, **kwargs):
        super(TeachForm, self).__init__(*args, **kwargs)
        self.fields['name'].required = False
        self.fields['age'].required = False
        self.fields['gender'].required = False
        self.fields['pic'].required = False
        self.fields['sub'].required = False