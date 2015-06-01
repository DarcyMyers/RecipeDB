# standard library imports
## none
# Core Django imports
from django.db import models
# Third-party imports
## none
# Project-specific imports
## none


class Recipe(models.Model):

    def __str__(self):
        return self.recipeName

    recipeName = models.CharField(max_length=128, verbose_name='Recipe Name') #allow super-long names
    description = models.TextField(null=True)
    dateFirstPrepared = models.DateField(verbose_name='Date First Prepared', null=True, blank=True)
    servings = models.PositiveIntegerField(null=True)
    instructions = models.TextField(null=True)
    vegetarian = models.NullBooleanField(verbose_name='Vegetarian?')
    prepTimeMinutes = models.PositiveIntegerField(null=True, verbose_name='Preparation Time (minutes)')
    cookTimeMinutes = models.PositiveIntegerField(null=True, verbose_name='Cook Time (minutes)')
    originalReference = models.TextField(null=True, verbose_name='Recipe Reference')
    NACHO_INDEX_CHOICES = (('Great', 'Completely awesome, definitely make again soon.'),
                            ('Good', 'Good, make this occasionally.'),
                            ('Ok', 'Ok, good if we need to use up ingredients.'))
    NachoIndex = models.CharField(max_length=5, choices=NACHO_INDEX_CHOICES, null=True, verbose_name='*Nacho* Index')
    image = models.ImageField(blank=True, null=True)




class Ingredient(models.Model):

    def __str__(self):
        return self.ingredientName

    ingredientName = models.CharField(max_length=20, null=True, verbose_name='Ingredient')
    ingredientNutritionContent = models.CharField(max_length=128, blank=True, null=True, verbose_name='Nutritional Content (Ingredient)') #allow super-long names

    class Meta:
        ordering = ('ingredientName',)
    pass


class MeasurementUnit(models.Model):

    def __str__(self):
        return self.unitName

    unitName = models.TextField(max_length=15, null=True, verbose_name='Unit')

    class Meta:
        ordering = ('unitName',)

    pass


class RecipeIngredientInfo(models.Model):

    #def __str__(self):
        #string = str(self.ingredientAmount) + ' ' + self.ingredientUnit + ' ' + str(self.ingredient) + ' ' + self.ingredientType
        #return string

    recipe = models.ForeignKey(Recipe)
    ingredient = models.ForeignKey(Ingredient)
    ingredientAmount = models.FloatField(verbose_name='Amount', null=True, blank=True)
    ingredientUnit = models.ForeignKey(MeasurementUnit)
    ingredientType = models.CharField(max_length=20, null=True, blank=True, verbose_name='Type')

    pass
