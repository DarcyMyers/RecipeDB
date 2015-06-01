from django.contrib import admin
from .models import Recipe, Ingredient, RecipeIngredientInfo, MeasurementUnit


class RecipeIngredientsInline(admin.TabularInline):
    model = RecipeIngredientInfo

class RecipeAdmin(admin.ModelAdmin):
    inlines = [RecipeIngredientsInline]


admin.site.register(RecipeIngredientInfo)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Ingredient)
admin.site.register(MeasurementUnit)
