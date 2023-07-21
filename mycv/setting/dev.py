from mycv.settings import *
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-*u4evsf7&61-gw4wy4b0$k&7uy83e%^po#bsbd49ak*w0c*x)&'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []
#INSTALLED_APPS=[]

SITE_ID=2

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

STATIC_ROOT= BASE_DIR / 'static'
STATICFILES_DIRS = [
    BASE_DIR / "statics",
    ]

MEDIA_ROOT=BASE_DIR/'media'
X_FRAME_OPTIONS = 'SAMEORIGIN'