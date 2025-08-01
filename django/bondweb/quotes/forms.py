from django import forms  # Import Django’s form utilities
from .models import Quote  # Import the Quote model we already created

# Create a form class based on the Quote model
class QuoteForm(forms.ModelForm):
    class Meta:
        model = Quote  # This form is based on the Quote model
        fields = ['text', 'author', 'category']  # These fields will show in the form
