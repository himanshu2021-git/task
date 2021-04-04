from django import forms
from .models import User, Employee

class UserAddForm(forms.ModelForm):
	class Meta:
		model = Employee
		fields = '__all__'

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['name'].queryset = User.objects.filter(user_type = 'Employee').all()

		for visible in self.visible_fields():
			visible.field.widget.attrs['class'] = 'form-control'

	