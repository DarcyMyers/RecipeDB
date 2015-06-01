from django.forms import ModelForm, Select, TextInput
from django.forms.models import inlineformset_factory
from .models import Recipe, RecipeIngredientInfo


IngredientsFormset = inlineformset_factory(Recipe, RecipeIngredientInfo, fk_name='recipe', fields= [
                #'recipe',
                #'id',
                'ingredient',
                'ingredientAmount',
                'ingredientUnit',
                'ingredientType'],
        widgets={
                #'recipe': None,
                #'id':None,
                'ingredient': Select,
                'ingredientAmount': None,
                'ingredientUnit': Select,
                'ingredientType': TextInput}, extra=10,)


class RecipeForm(ModelForm):
    class Meta:
        model = Recipe
        fields = ['recipeName',
                  'description',
                  'image',
                  'dateFirstPrepared',
                  'servings',
                  'instructions',
                  'vegetarian',
                  #'ingredients',
                  'prepTimeMinutes',
                  'cookTimeMinutes',
                  'originalReference',
                  'NachoIndex',
                  ]




## todo: lookinto the below blogpost to see if applicable to 'nested formset approach'
#reference: http://whoisnicoleharris.com/2015/01/06/implementing-django-formsets.html
