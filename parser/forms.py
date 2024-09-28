from django import forms
from . import models, rezka_parser


class ParserForm(forms.Form):
    MEDIA_CHOICES = (
        ('manas.kg', 'manas.kg'),
    )
    media_type = forms.ChoiceField(choices=MEDIA_CHOICES)

    class Meta:
        fields = [
            'media_type',
        ]

    def parser_data(self):
        if self.data['media_type'] == 'manas.kg':
            rezka_pars = rezka_parser.parsing()
            for i in rezka_pars:
                models.ManasFilm.objects.create(**i)