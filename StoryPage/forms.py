from django import forms

class NewChoiceForm(forms.Form):
    choice_text = forms.CharField(label='choice_text', max_length=100)
    plot_point_text = forms.CharField(label='plotpoint-text', max_length=1000)
    plot_point_id = forms.IntegerField(label='plot_point_id')
    author = forms.CharField(label='author', max_length=20)

class OpenPlotPointForm(forms.Form):
    destination_id = forms.IntegerField(label='destination_id')


