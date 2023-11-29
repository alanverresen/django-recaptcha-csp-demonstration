from django.urls import path

from . import views


app_name = "myapp"
urlpatterns = [
    path("", views.index, name="index"),
    path("v2checkbox", views.v2checkbox, name="v2checkbox"),
    path("v2checkbox_w_csp", views.v2checkbox_w_csp, name="v2checkbox_w_csp"),
    path("v2invisible", views.v2invisible, name="v2invisible"),
    path("v2invisible_w_csp", views.v2invisible_w_csp, name="v2invisible_w_csp"),
    path("v3", views.v3, name="v3"),
    path("v3_w_csp", views.v3_w_csp, name="v3_w_csp"),
]
