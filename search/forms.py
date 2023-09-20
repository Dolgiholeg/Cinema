from django import forms

class Kinofilm(forms.Form):
    country1 = forms.CharField(label='СТРАНА ПРОИЗВОДИТЕЛЬ', max_length=20)
    name1 = forms.CharField(label='НАЗВАНИЕ ФИЛЬМА',max_length=30)
    year1 = forms.IntegerField(label='ГОД ВЫПУСКА',max_value=2023, min_value=1)

class Kinofilmcountry(forms.Form):
    country1 = forms.CharField(label='СТРАНА ПРОИЗВОДИТЕЛЬ', max_length=20, help_text='напишите страну производителя фильмов для поиска')

class Kinofilmyear(forms.Form):
    year1 = forms.IntegerField(label='ГОД ВЫПУСКА', max_value=2023, min_value=1, help_text='напишите год выпуска фильмов для поиска')

class Kinofilmnoyear(forms.Form):
    year1 = forms.IntegerField(label='ГОД ВЫПУСКА', max_value=2023, min_value=1, help_text='напишите год выпуска фильмов для исключения при поиске')