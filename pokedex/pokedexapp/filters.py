from django.db.models import Q
import django_filters
from models import Pokemon


class LocationFilter(django_filters.FilterSet):
    search = django_filters.CharFilter(method='search_filter')

    class Meta:
        model = Pokemon
        fields = ['search']

    def search_filter(self, queryset, name, value):
        return queryset.filter(
            Q(nom__icontains=value) | Q(types__nom__icontains=value)
        )