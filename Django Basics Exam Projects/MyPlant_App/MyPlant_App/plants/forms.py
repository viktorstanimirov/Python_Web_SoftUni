from django import forms

from MyPlant_App.plants.models import Plant


class PlantBaseForm(forms.ModelForm):
    class Meta:
        model = Plant
        fields = "__all__"
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'description': forms.Textarea(
                attrs={
                    'class': 'form-control'
                }
            ),
            'image': forms.FileInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'price': forms.NumberInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'category': forms.Select(
                attrs={
                    'class': 'form-control'
                }
            ),
        }


class PlantCreateForm(PlantBaseForm):
    pass


class PlantUpdateForm(PlantBaseForm):
    pass


class PlantDeleteForm(PlantBaseForm):
    pass


class PlantDetailForm(PlantBaseForm):
    pass
