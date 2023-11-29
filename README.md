# django-recaptcha + django-csp

The goal of this project is to demonstrate how converting the inline scripts
used by `django-recaptcha` for its widgets to external scripts, addresses
[issue 101](https://github.com/django-recaptcha/django-recaptcha/issues/101).


## Setup
To install this project with the relevant fork of `django-recaptcha`, prepare
the following first:

- get a pair of keys for reCAPTCHA v3 through reCAPTCHA's admin console
    - add `localhost`, `127.0.0.1`, or equivalent to domains
    - store the keys in `secrets.json` (see below)
- prepare an isolated environment to install and run the project (e.g. 
    [venv](https://docs.python.org/3/library/venv.html))

The file `secrets.json` should be located in your the repository's root 
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


## Usage
Once the application is up and running, try the different widgets:

- open the browser's developer tools to check for CSP problems
    - there should be none
- after clicking the submit button, the following is shown:
    - whether the form was valid
    - the data that was submitted

You can uninstall the fork of `django-recaptcha`, and install the most current 
package of `django-recaptcha` to demonstrate the errors.
