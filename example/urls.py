from django.conf.urls import url

from app.views import (
    DefaultFormByFieldView,
)

urlpatterns = [

    url(r"^form_by_field$", DefaultFormByFieldView.as_view(), name="form_by_field"),
]
