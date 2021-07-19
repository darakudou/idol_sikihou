from bootstrap_datepicker_plus import DatePickerInput
from django import forms


class SetlistForecastForm(forms.Form):

    date = forms.DateField(
        label="開催日",
        widget=DatePickerInput(
            format='%Y-%m-%d',
            options={
                'locale': 'ja',
                'dayViewHeaderFormat': 'YYYY年 MMMM'}),
    )
    is_main = forms.BooleanField(label="主催か?", required=False)
    live_time = forms.ChoiceField(
        label="出演時間",
        choices=(
            ('15分', '15分'),
            ('25分', '25分'),
            ('30分', '30分'),
            ('40分', '40分'),
        ),
        required=True,
        widget=forms.widgets.Select
        )
    OPTIONS = (
        ("a", "A"),
        ("b", "B"),
    )
    # todo: 後でここは共演したアイドルモデルから持ってくるようにする
    other_idol = forms.MultipleChoiceField(
        label="共演者",
        required=False,
        widget=forms.CheckboxSelectMultiple,
        choices=OPTIONS)
    setlists = forms.CharField(
        label="セットリスト",
        required=False,
        widget=forms.TextInput(
            attrs={'readonly': 'readonly'}
        ))
