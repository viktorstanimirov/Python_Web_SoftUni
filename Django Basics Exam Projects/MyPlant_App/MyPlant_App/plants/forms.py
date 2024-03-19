from django import forms

from MyPlant_App.core.form_mixins import ReadonlyFieldsFormMixin
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


class PlantsDeleteForm(ReadonlyFieldsFormMixin, PlantBaseForm):
    readonly_fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._apply_readonly_on_fields()

    def save(self, commit=True):
        if commit:
            # self.instance.comment.delete()
            # self.instance.likes.delete()
            self.instance.delete()
        return self.instance



