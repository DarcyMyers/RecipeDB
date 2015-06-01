from django.shortcuts import render, redirect, get_object_or_404
from .models import Recipe, Ingredient, RecipeIngredientInfo
from .forms import RecipeForm, IngredientsFormset


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
    ingredients = RecipeIngredientInfo.objects.filter(recipe=recipe)
    context = {'recipe': recipe, 'ingredients':ingredients}
    return render(request, 'viewrecipe.html', context)


def add_recipe(request):
    # Add a new recipe and save data submitted through the form to the database
    recipeform = RecipeForm()
    ingredientsformset = IngredientsFormset()


    # for adding a recipe
    if request.method == 'POST':
        recipeform = RecipeForm(request.POST)

        if recipeform.is_valid():
            # saves the valid recipeform so that recipe can be passed as instance to the ingredientformset
            recipeSaved = recipeform.save()
            ingredientsformset = IngredientsFormset(request.POST, request.FILES, instance=recipeSaved)
            if ingredientsformset.is_valid():
                ingredientsformset.save()

        return redirect(list_recipes)


    context = {
        'recipeform': recipeform,
        'ingredientsformset': ingredientsformset,
        }
    return render(request, 'addrecipe.html', context)



def edit_recipe(request, recipe_id):
    # Edit existing recipe and save data submitted through the form to the database

    # for editing a recipe
    recipeToUpdate = get_object_or_404(Recipe, pk=recipe_id)
    recipeform = RecipeForm(instance=recipeToUpdate)
    ingredientsformset = IngredientsFormset(instance=recipeToUpdate)

    if request.method == 'POST':
        recipeform = RecipeForm(request.POST, instance=recipeToUpdate)

        if recipeform.is_valid():
            # saves the valid recipeform so that recipe can be passed as instance to the ingredientformset
            recipeSaved = recipeform.save(commit=False)
            ingredientsformset = IngredientsFormset(request.POST, request.FILES, instance=recipeSaved)

            if ingredientsformset.is_valid():
                recipeSaved.save()
                ingredientsformset.save()

            return redirect(list_recipes)


    context = {'recipeform': recipeform, 'ingredientsformset': ingredientsformset,}
    return render(request, 'editrecipe.html', context)

