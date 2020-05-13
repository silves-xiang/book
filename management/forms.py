from django import forms
from management.models import Book,Image
class BookForm(forms.ModelForm):
	class Meta:
		model=Book
		fields=['text']