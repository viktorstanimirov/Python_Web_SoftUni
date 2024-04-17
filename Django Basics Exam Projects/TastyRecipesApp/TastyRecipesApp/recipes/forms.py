from django import forms

from TastyRecipesApp.core.form_mixin import ReadonlyFieldsFormMixin
from TastyRecipesApp.recipes.models import Recipe


# class RecipeModelForm(forms.ModelForm):
#     class Meta:
#         model = Recipe
#         fields = ['title', 'cuisine_type', 'ingredients', 'instructions', 'cooking_time', 'image_url']
#         widgets = {
#             'ingredients': forms.Textarea(attrs={'placeholder': 'ingredient1, ingredient2, ...'}),
#             'instructions': forms.Textarea(attrs={'placeholder': 'Enter detailed instructions here...'}),
#             'image_url': forms.URLInput(attrs={'placeholder': 'Optional image URL here...'}),
#         }
#         help_texts = {
#             'cooking_time': 'Provide the cooking time in minutes.',
#             "ingredients": "Ingredients must be separated by a comma and space.",
#         }
#         labels = {
#             'image_url': 'Image URL',
#         }
#
#
# class CreateRecipeForm(RecipeModelForm):
#     pass

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'cuisine_type', 'ingredients', 'instructions', 'cooking_time', 'image_url']
        widgets = {
            'ingredients': forms.Textarea(attrs={'placeholder': 'ingredient1, ingredient2, ...'}),
            'instructions': forms.Textarea(attrs={'placeholder': 'Enter detailed instructions here...'}),
            'image_url': forms.URLInput(attrs={'placeholder': 'Optional image URL here...'}),
        }
        help_texts = {
            'ingredients': 'Ingredients must be separated by a comma and space.',
            'cooking_time': 'Provide the cooking time in minutes.',
        }


class RecipeUpdateForm(RecipeForm):
    pass


class RecipeDeleteForm(RecipeForm, ReadonlyFieldsFormMixin):
    readonly_fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._apply_readonly_on_fields()

    def save(self, commit=True):
        if commit:
            self.instance.delete()
        return self.instance