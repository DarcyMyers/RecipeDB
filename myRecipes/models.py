from django.db import models


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

    pass


class Ingredient(models.Model):

    def __str__(self):
        return self.ingredientName

    ingredientName = models.TextField(null=True, verbose_name='Ingredient')
    ingredientNutritionContent = models.CharField(max_length=128, blank=True, null=True, verbose_name='Nutritional Content (Ingredient)') #allow super-long names

    pass


class RecipeIngredientInfo(models.Model):

    def __str__(self):
        string = str(self.ingredientAmount) + ' ' + self.ingredientUnit + ' ' + str(self.ingredient) + ' ' + self.ingredientType
        return string

    recipe = models.ManyToManyField(Recipe, related_name='ingredients')
    ingredient = models.ManyToManyField(Ingredient)
    ingredientAmount = models.FloatField(verbose_name='Amount')
    ingredientUnit = models.CharField(max_length=10, null=True, verbose_name='Unit')
    ingredientType = models.CharField(max_length=10, null=True, blank=True, verbose_name='Type')


