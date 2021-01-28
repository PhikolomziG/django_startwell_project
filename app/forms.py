from django import forms

from .models import Child


class DateInput(forms.DateInput):
	input_type = 'date'


class DateCreator():
	my_date_field = forms.DateField(widget=DateInput)


class ChildForm(forms.ModelForm):
	class Meta:
		model = Child
		fields = [
		'Name',
		'Surname',
		'DateOfBirth',
		'StartDate',
		'Gender',
		'Consent',
		'School'
		]

		widgets = {

		'Name': forms.TextInput(attrs={'class': 'form-control'}),
		'Surname': forms.TextInput(attrs={'class': 'form-control'}),
		'DateOfBirth': DateInput(attrs={'class': 'form-control'}),
		'StartDate': DateInput(attrs={'class': 'form-control'}),
		'Gender': forms.Select(attrs={'class': 'form-control'}),
		'Consent': forms.Select(attrs={'class': 'form-control'}),
		'School': forms.TextInput(attrs={'class': 'form-control'})


		}





	




