# from material.forms import forms
import json
import logging

from botapp import models as bot_models
from datastore import models as data_models
from django import forms
from django.forms import BaseInlineFormSet

logger = logging.getLogger(__name__)
#
#
# class DateParameterForm(forms.ModelForm):
#     model = bot_models.DateParameterModel
#     data_value = forms.DateTimeField()
#
#     def __init__(self, *args, **kwargs):
#         super(DateParameterForm, self).__init__(*args, **kwargs)
#         self.fields['data_value'].label = self.instance.argument.display_name
#         self.fields['data_value'].initial = bot_models.DatePropertyModel.objects.get(pk=self.instance.argument.pk).default_value
#         logger.debug('render date-parameter: %s = %s' % (self.instance.argument.name, self.instance.current_value))
#
# class EnumerationParameterForm(forms.ModelForm):
#     model = bot_models.EnumerationParameterModel
#     data_value = forms.ModelChoiceField(bot_models.EnumerationValueModel.objects.all())
#
#     def __init__(self, *args, **kwargs):
#         super(EnumerationParameterForm, self).__init__(*args, **kwargs)
#         self.fields['data_value'].label = self.instance.argument.display_name
#         enumeration_property = bot_models.EnumerationPropertyModel.objects.get(pk=self.instance.argument.pk)
#         self.fields['data_value'].choices = [(e.pk, e.display_name) for e in enumeration_property.group.values]
#         logger.debug('render enumeration-parameter: %s = %s' % (self.instance.argument.name, self.instance.current_value))
#
# class NumberParameterForm(forms.ModelForm):
#     model = bot_models.NumberParameterModel
#     data_value = forms.IntegerField()
#
#     def __init__(self, *args, **kwargs):
#         super(NumberParameterForm, self).__init__(*args, **kwargs)
#
#         property = bot_models.NumberPropertyModel.objects.get(pk=self.instance.argument.pk)
#
#         self.fields['data_value'].initial = property.default_value
#         self.fields['data_value'].label = self.instance.argument.display_name
#         logger.debug('render numeric-parameter: %s = %s' % (self.instance.argument.name, self.instance.current_value))
#
# class TextParameterForm(forms.ModelForm):
#     model = bot_models.TextParameterModel
#     data_value = forms.CharField()
#
#     def __init__(self, *args, **kwargs):
#         super(TextParameterForm, self).__init__(*args, **kwargs)
#         self.fields['data_value'].label = self.instance.argument.display_name
#         self.fields['data_value'].initial = bot_models.TextPropertyModel.objects.get(pk=self.instance.argument.pk).default_value
#         logger.debug('render text-parameter: %s = %s' % (self.instance.argument.name, self.instance.current_value))

from django.forms import BaseInlineFormSet


class BestOfferInputForm(forms.ModelForm):
    class Meta:
        model = data_models.BestOfferModel
        fields = ['timestamp', 'duration', 'supplier', 'market', 'departure', 'arrival']

#
# class ScheduleForm(forms.ModelForm):
#     class Meta:
#         model = bot_models.BestOfferJobModel
#         fields = ['input']
    # portal = forms.ModelChoiceField(label='Portal', queryset=bot_models.PortalModel.objects.all())


    # date = forms.DateTimeField(label='Travel date')
    # duration = forms.IntegerField(label='Travel duration')
    # competitors = forms.ModelMultipleChoiceField(label='Competitors', queryset=ProjectModel.objects.all())
    # hotels = forms.ModelMultipleChoiceField(label='Hotels', queryset=HotelModel.objects.all())
    # boards = forms.ModelMultipleChoiceField(label='Boardtypes', queryset=BoardModel.objects.all())
    # bag_types = forms.ModelMultipleChoiceField(label='Bagtypes', queryset=BagTypeModel.objects.all())
    # room_types = forms.ModelMultipleChoiceField(label='Roomtypes', queryset=RoomTypeModel.objects.all())


#
# class UploadFileForm(forms.Form):
#     file = forms.FileField()
#

class LuaSourceForm(forms.Form):
    file = forms.FileField(
        label='Select a file',
        help_text='max. 2 megabytes',
        widget=forms.FileInput
    )
