from django.contrib import admin
from .models import Recipe, Ingredient, RecipeIngredientInfo


class RecipeIngredientsInline(admin.TabularInline):
    model = RecipeIngredientInfo.ingredient.through

class RecipeIngredientInfoAdmin(admin.ModelAdmin):
    inlines = [RecipeIngredientsInline]


admin.site.register(RecipeIngredientInfo, RecipeIngredientInfoAdmin)
admin.site.register(Recipe)
admin.site.register(Ingredient)
