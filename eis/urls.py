from django.urls import path

from eis.views import IndexView

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
]
