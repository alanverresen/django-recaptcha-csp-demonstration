from django.forms import Form
from django.conf import settings
from django_recaptcha.fields import ReCaptchaField
from django_recaptcha.widgets import ReCaptchaV2Checkbox
from django_recaptcha.widgets import ReCaptchaV2Invisible
from django_recaptcha.widgets import ReCaptchaV3


class V2CheckboxForm(Form):
    captcha = ReCaptchaField(
        widget=ReCaptchaV2Checkbox())


class V2InvisibleForm(Form):
    captcha = ReCaptchaField(
        widget=ReCaptchaV2Invisible())


class V3Form(Form):
    captcha = ReCaptchaField(
        private_key=settings.SECRETS["recaptcha_v3_private_key"],
        public_key=settings.SECRETS["recaptcha_v3_public_key"],
        widget=ReCaptchaV3(action="hello")
    )
