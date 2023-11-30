# django-recaptcha + django-csp

The goal of this project is to demonstrate how the conversion of the inline 
scripts used by `django-recaptcha`'s widgets to external scripts addresses
[issue 101](https://github.com/django-recaptcha/django-recaptcha/issues/101).


## Setup
Before getting started, clone this project and make sure to prepare the 
following:

- store keys for reCAPTCHA v3 in `secrets.json` (see below)
    - you can get a pair of keys for reCAPTCHA v3 through reCAPTCHA's admin 
      console
    - do not forget to add `localhost`, `127.0.0.1`, or whatever applies to the 
      list of domains through reCAPTCHA's admin console
- prepare an isolated environment to install and run the project (e.g. 
    [venv](https://docs.python.org/3/library/venv.html))

The file `secrets.json` should be located within the repository's root
directory, and should have the following structure:

```
{
  "recaptcha_v3_public_key": "<PUBLIC KEY HERE!>",
  "recaptcha_v3_private_key": "<PRIVATE KEY HERE!>"
}
```

After making the necessary preparations, set up the project as follows:

0. activate your virtual environment
1. `$ python3 -m pip install -r requirements.txt`
2. `$ python3 manage.py runserver`
3. open the web application in your web browser

**NOTE** This will install [the relevant fork of `django-recaptcha`](https://github.com/alanverresen/django-recaptcha/tree/issue101-externalscripts).
instead of the latest `django-recaptcha` package.
Install the latest `django-recaptcha` package instead if you want to
demonstrate the CSP errors.


## Usage
Once the application is up and running, you can try the different widgets 
with CSP enabled and disabled:

- open the browser's developer tools to check for CSP problems
    - there should be none for any of the widgets
- after clicking the submit button, the following is shown:
    - whether the form was valid
    - the data that was submitted
