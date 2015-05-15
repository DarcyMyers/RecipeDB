from django.shortcuts import render, HttpResponse, redirect, get_object_or_404, render_to_response
from .models import Recipe, Ingredient, RecipeIngredientInfo
from .forms import RecipeForm
from django.forms import modelformset_factory



def list_recipes(request):
    # Pull the current list of all recipes and return them
#     return HttpResponse("This will be a list of all recipes.")
    recipelist = Recipe.objects.all()
    context = {
        'recipelist': recipelist,
        }
    return render(request, 'listrecipes.html', context)


# For viewing a recipe by recipe 'name'/ID
def view_recipe(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    context = {'recipe': recipe}
    return render(request, 'viewrecipe.html', context)



def add_recipe(request):
    # A form that can be used to add a new recipe.
    # Save data submitted through the form to the database as a new recipe

    ingredientListFormSet = modelformset_factory(RecipeIngredientInfo, fields=('recipe',
                                                                                     'ingredient',
                                                                                     'ingredientAmount',
                                                                                     'ingredientUnit',
                                                                                     'ingredientType'))

    if request.method == 'POST':
        ingredientListFormSet(request.POST, request.FILES)
        if ingredientListFormSet.is_valid():
            instances = ingredientListFormSet.save(commit=False)
            for instance in instances:
                instance.save()
                ingredientListFormSet.save_m2m()


    recipeform = RecipeForm(request.POST or None)
    if recipeform.is_valid():
        recipe = recipeform.save(commit=False)
        recipe.save()
        recipeform.save_m2m()
        return redirect(list_recipes)

    context = {'recipeform': recipeform, 'ingredientListFormSet': ingredientListFormSet,}
    return render(request, 'addrecipe.html', context)
    #return render_to_response('addrecipe.html', context)