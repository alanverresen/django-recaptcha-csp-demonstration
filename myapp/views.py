from csp.decorators import csp_exempt, csp_update
from django.shortcuts import redirect, render

from . import forms


def index(request):
    return render(request, "myapp/index.html")


@csp_exempt
def v2checkbox(request):
    return _handle_form(request, forms.V2CheckboxForm)


@csp_update(
    SCRIPT_SRC=["'self'", "https://www.google.com/recaptcha/", "https://www.gstatic.com/recaptcha/"],
    FRAME_SRC=["'self'", "https://www.google.com/recaptcha/", "https://recaptcha.google.com/recaptcha/"],
)
def v2checkbox_w_csp(request):
    return _handle_form(request, forms.V2CheckboxForm)


@csp_exempt
def v2invisible(request):
    return _handle_form(request, forms.V2InvisibleForm)


@csp_update(
    SCRIPT_SRC=["'self'", "https://www.google.com/recaptcha/", "https://www.gstatic.com/recaptcha/"],
    FRAME_SRC=["'self'", "https://www.google.com/recaptcha/", "https://recaptcha.google.com/recaptcha/"],
)
def v2invisible_w_csp(request):
    return _handle_form(request, forms.V2InvisibleForm)


@csp_exempt
def v3(request):
    return _handle_form(request, forms.V3Form)


@csp_update(
    SCRIPT_SRC=["'self'", "https://www.google.com/recaptcha/", "https://www.gstatic.com/recaptcha/"],
    FRAME_SRC=["'self'", "https://www.google.com/recaptcha/", "https://recaptcha.google.com/recaptcha/"],
)
def v3_w_csp(request):
    return _handle_form(request, forms.V3Form)


def _handle_form(request, form_type):
    if request.method == "POST":
        form = form_type(request.POST)
        context = {
            "is_valid": form.is_valid(),
            "data": form.data,
        }
        return render(request, "myapp/results.html", context)
    else:
        context = {
            "form": form_type(),
        }
        return render(request, "myapp/form.html", context)
