from django import forms

from codetest.models import User
import datetime

class RegistrationForm(forms.ModelForm):
    def year_choices():
        year = [('','Year')]
        for r in range(1984, datetime.date.today().year+1):
            year.append((r,r))
        return year
    
    MONTH = [
        ('','Month'),
        ('1','January'),
        ('2','February'),
        ('3','March'),
        ('4','April'),
        ('5','May'),
        ('6','June'),
        ('7','July'),
        ('8','August'),
        ('9','September'),
        ('10','October'),
        ('11','November'),
        ('12','December'),
    ]

    month = forms.ChoiceField(choices=MONTH, initial='Month', required=False)
    year = forms.ChoiceField(choices=year_choices, initial='Year', required=False)
    class Meta:
        model = User
        fields = [
            'mobile_number',
            'first_name',
            'last_name',
            'date_of_birth',
            'gender',
            'email'
        ]

        GENDER = [('Male','Male'), ('Female','Female')]
        widgets = {
            'mobile_number' : forms.TextInput(attrs={'placeholder':'Mobile Number','pattern':'\+?([ -]?\d+)+|\(\d+\)([ -]\d+)','title':'Please enter valid Indonesian phone number'}),
            'first_name'    : forms.TextInput(attrs={'placeholder':'First Name'}),
            'last_name'     : forms.TextInput(attrs={'placeholder':'Last Name'}),
            'date_of_birth' : forms.DateInput(),
            'gender'        : forms.RadioSelect(choices=GENDER),
            'email'         : forms.EmailInput(attrs={'placeholder':'Email'})
        }
    
    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'