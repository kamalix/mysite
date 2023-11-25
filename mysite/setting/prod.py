from mysite.settings import *

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-+1pr5*=^z=9$nz2h$b+k)msn8&0=n#ebk^lb5q910^b0e@cqr='

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['kamal-amani.ir','www.kamal-amani.ir']

#INSTALLED_APPS = []


#site framework
SITE_ID = 2

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

STATIC_ROOT =BASE_DIR/'static'
MEDIA_ROOT =BASE_DIR/'media'


STATICFILES_DIRS = [
    BASE_DIR / "statics",   
]




#CSRF_COOKIE_SECURE = True