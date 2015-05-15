from django.forms import ModelForm
from .models import Recipe, RecipeIngredientInfo, Ingredient

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
                  'NachoIndex']

    def __init__(self, *args, **kwargs):
        super(RecipeForm, self).__init__(*args, **kwargs)
        #self.fields["ingredients"].queryset = Ingredient.objects.all()