import django_filters
from django_filters import DateFilter, CharFilter

from django.db.models import Q

from django import forms
from .models import Diary

class DateInput(forms.DateInput):
    input_type = 'date'

class DiaryFilter(django_filters.FilterSet):
    start_date = DateFilter(field_name="date_created", lookup_expr="gte", widget = DateInput())
    end_date = DateFilter(field_name="date_created", lookup_expr="lte", widget = DateInput())
    title = CharFilter(field_name="title", lookup_expr="icontains")
    diary_entry = CharFilter(field_name="diary_entry", lookup_expr="icontains")


    class Meta:
        model = Diary
        fields = '__all__'


