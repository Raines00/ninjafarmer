from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django import forms
from . models import Farm, Staff, Department,Produce,TimeLine,Sales,Debtors,Activities,Expenses
from django.contrib.auth import get_user_model


class LoginForm (AuthenticationForm):
    username = forms.CharField(max_length=10,widget=forms.TextInput(attrs={'class':'form-control p-4 mb-3', 'placeholder':'Username '}))
    password = forms.CharField(max_length=20, widget=forms.PasswordInput(attrs={'class':'form-control p-4 mb-3', 'placeholder':'Password '}))

    class Meta:
        model = get_user_model()
        fields = '__all__'
class RegisterForm (UserCreationForm):
    first_name = forms.CharField(max_length=15, widget=forms.TextInput(attrs={'class':'form-control p-4 mb-3', 'placeholder':'First Name '}))
    last_name = forms.CharField(max_length=15, widget=forms.TextInput(attrs={'class':'form-control p-4 mb-3', 'placeholder':'Last Name '}))
    username = forms.CharField(max_length=10,widget=forms.TextInput(attrs={'class':'form-control p-4 mb-3', 'placeholder':'Username '}))
    password1 = forms.CharField(label='Password',max_length=20, widget=forms.PasswordInput(attrs={'class':'form-control p-4 mb-3', 'placeholder':'Password '}))
    password2 = forms.CharField(label='Confirm Password',max_length=20, widget=forms.PasswordInput(attrs={'class':'form-control p-4 mb-3', 'placeholder':'Confirm Password '}))

    class Meta:
        model = get_user_model()
        fields = ['first_name','last_name','username','password1','password2','image']

class FarmForm (forms.ModelForm):

    class Meta:
        model = Farm
        fields = '__all__'
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Farm Unique Name'}),
            'image':forms.FileInput(attrs={'class':'form-control'}),
            'no_produce':forms.TextInput(attrs={'class':'form-control', 'placeholder':'No of Produce in this Farm'}),
            'produce_categories':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Categories'}),
            'location':forms.Textarea(attrs={'class':'form-control text-justify', 'placeholder':'Farm Location','rows':2}),
            'about':forms.Textarea(attrs={'class':'form-control', 'placeholder':'More Info','rows':2}),
        }

class StaffForm(forms.ModelForm):

    class Meta:
        model = Staff
        fields = "__all__"
        widgets={
            
            'first_name':forms.TextInput(attrs={'class':'form-control','placeholder':'First Name'}),
            'last_name':forms.TextInput(attrs={'class':'form-control','placeholder':'Last Name'}),
            'stipend':forms.TextInput(attrs={'class':'form-control','placeholder':'Salary'}),
            'mobile_number':forms.TextInput(attrs={'class':'form-control','placeholder':'Mobile Number'}),
            'state':forms.Select(attrs={'class':'form-control','placeholder':'Salary'}),
            'country':forms.TextInput(attrs={'class':'form-control','placeholder':'country'}),
            'department':forms.Select(attrs={'class':'form-control','placeholder':''}),
            'work_description':forms.Textarea(attrs={'class':'form-control','placeholder':'Work Description','rows':2, 'cols':4}),
            'image':forms.FileInput(attrs={'class':'form-control'}),
        }

class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = '__all__'
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control','placeholder':'Department Name'}),
            'description':forms.Textarea(attrs={'class':'form-control', 'placeholder':'Description'})
        }

class ProduceForm(forms.ModelForm):
    class Meta:
        model = Produce
        fields = '__all__'
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control','placeholder':'Produce Name'}),
            'types':forms.TextInput(attrs={'class':'form-control mb-2','placeholder':'Produce Type'}),
            'HarvestDate':forms.TextInput(attrs={'class':'form-control mb-3 ','placeholder':'Harvest Date'}),
            'total':forms.NumberInput(attrs={'class':'form-control mb-3','placeholder':'Total'}),
            'ímage':forms.FileInput(attrs={'class':'form-control mt-2'})
        }

class HarvestForm(forms.ModelForm):
    class Meta:
        model = TimeLine
        fields = '__all__'
        widgets = {
            'number':forms.NumberInput(attrs={'class':'form-control','placeholder':'Total Number of Produce Harvested'}),
            'farm':forms.TextInput(attrs={'class':'form-control','placeholder':'From which Farm'}),
            'others':forms.Textarea(attrs={'class':'form-control','placeholder':'Other Note here'})
        }

class SalesForm(forms.ModelForm):
    class Meta:
        model = Sales
        fields =['types','customer','quantity','amount','price']
        widgets = {
            'types':forms.TextInput(attrs={'class':'form-control','placeholder':'e.g Tomatoes'}),
            'amount':forms.NumberInput(attrs={'class':'form-control','placeholder':'Price per unit','id':'amt'}),
            'customer':forms.TextInput(attrs={'class':'form-control','placeholder':'Anonymous'}),
            'quantity':forms.NumberInput(attrs={'class':'form-control','placeholder':'Total Number of Produce','id':'qty'}),
            'price':forms.NumberInput(attrs={'class':'form-control','placeholder':'Total Amount to be paid','id':'prc','readonly':'readonly'})

        }

class ActivitiesForm(forms.ModelForm):
    class Meta:
        model = Activities
        fields = '__all__'
        widgets = {
            'date':forms.DateInput(format=('%d-%m-%Y'),attrs={'class': 'datepicker', 'placeholder': 'Select a date', 'type': 'date'}),
            'activity1':forms.TextInput(attrs={'class':'form-control','placeholder':'Activity 1','id':'activity1'}),
            'activity2':forms.TextInput(attrs={'class':'form-control','placeholder':'Activity 2','id':'activity2'}),
            'activity3':forms.TextInput(attrs={'class':'form-control','placeholder':'Activity 3','id':'activity3'}),
            'activity4':forms.TextInput(attrs={'class':'form-control','placeholder':'Activity 4','id':'activity4'})

        }

class ExpensesForm(forms.ModelForm):
    class Meta:
        model = Expenses
        fields = '__all__'
        widgets = {
            'date':forms.DateInput(format=('%d-%m-%Y'),attrs={'class': 'datepicker', 'placeholder': 'Select a date', 'type': 'date'}),
            'activity':forms.TextInput(attrs={'class':'form-control','placeholder':'Activity Name','id':'activity'}),
            'investment':forms.NumberInput(attrs={'class':'form-control','placeholder':'Amount Spent','id':'investment'})

        }


class DebtorsForm(forms.ModelForm):
    class Meta:
        model = Debtors
        fields = '__all__'
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control','placeholder':'Full Name'}),
            'file_no':forms.TextInput(attrs={'class':'form-control','placeholder':'Staff-file No'}),
            'quantity':forms.NumberInput(attrs={'class':'form-control','placeholder':'Total Number of Produce'}),
            'department':forms.TextInput(attrs={'class':'form-control','placeholder':'Staffer Department' }),
            'amount':forms.NumberInput(attrs={'class':'form-control','placeholder':'Total Amount to be paid'}),
            'signature':forms.ClearableFileInput(attrs={'class':'form-control'})

        }
        