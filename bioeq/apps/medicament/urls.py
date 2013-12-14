from django.conf.urls import patterns, url
from django_filters.views import FilterView

from .filters import ProductFilter

urlpatterns = patterns(
    '',
    (r'^list/$', FilterView.as_view(filterset_class=ProductFilter)),
)
