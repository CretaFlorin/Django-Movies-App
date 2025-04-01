import re
from viewer.models import Genre, Movie
from django.forms import CharField, DateField, Form, IntegerField, ModelChoiceField, ModelForm, Textarea, ValidationError, SelectDateWidget

# class MovieForm(Form):
#     title = CharField(max_length=128)
#     rating = IntegerField(min_value=1, max_value=10)
#     released = DateField(widget=SelectDateWidget)
#     genre = ModelChoiceField(queryset=Genre.objects)
#     description = CharField(widget=Textarea, required=False)
    
#     # Force each sentence of the description to be capitalized.
#     def clean_description(self):
#         initial = self.cleaned_data['description']
#         sentences = re.sub(r'\s*\.\s*', '.', initial).split('.')
#         return '. '.join(sentence.capitalize() for sentence in sentences)
    
#     def clean(self):
#         result = super().clean()
#         if result['genre'].name.lower() == 'comedy' and result['rating'] > 5:
#             raise ValidationError(
#                 "Commedies aren't so good to be rated over 5."
#             )
#         return result
    
# 2. Handling Data with Modelform
class MovieForm(ModelForm):
    class Meta:
        model = Movie
        fields = '__all__'
    
    rating = IntegerField(min_value=1, max_value=10)
    
    # Force each sentence of the description to be capitalized.
    def clean_description(self):
        initial = self.cleaned_data['description']
        sentences = re.sub(r'\s*\.\s*', '.', initial).split('.')
        return '. '.join(sentence.capitalize() for sentence in sentences)
    
    def clean(self):
        result = super().clean()
        if result['genre'].name.lower() == 'comedy' and result['rating'] > 5:
            raise ValidationError(
                "Commedies aren't so good to be rated over 5."
            )
        return result

