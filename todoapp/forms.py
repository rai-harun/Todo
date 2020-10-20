from django.forms import ModelForm
from .models import Todo

class TodoForm(ModelForm):
    class Meta:
        model = Todo
        fields = '__all__'
        localized_fields = ('created_date',)