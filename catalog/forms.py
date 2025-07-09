from django.core.exceptions import ValidationError
from django.forms import ModelForm

from catalog.models import Product, Category

FORBIDDEN_WORDS = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)

        self.fields['name'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите имя'
        })

        self.fields['description'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите описание'
        })

        self.fields['category'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Выберите категорию'
        })

        self.fields['price'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите цену'
        })

        self.fields['photo'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Вставьте photo'
        })

        self.fields['created_at'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите дату'
        })

        self.fields['updated_at'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите дату'
        })

        self.fields['category'].widget.attrs.update({
            'class': 'form-control',
        })

    def clean_name(self):
        name = self.cleaned_data.get('name')
        for word in FORBIDDEN_WORDS:
            if word.lower() in name.lower():
                raise ValidationError(f'Название содержит запрещенное слово: {word}')
        return name

    def clean_description(self):
        description = self.cleaned_data.get('description')
        for word in FORBIDDEN_WORDS:
            if word.lower() in description.lower():
                raise ValidationError(f'Описание содержит запрещенное слово: {word}')
        return description

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price is not None and price < 0:
            raise ValidationError('Цена не может быть отрицательной')
        return price

class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = "__all__"

