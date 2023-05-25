DEBUG = False

ROOT_URLCONF = "app.urls"
STATIC_URL = "/staic/"

INSTALLED_APPS = [
    # core app
    "django.contrib.admin",
    "django.contrib.contenttypes",
    "django.contrib.auth",
    "django.contrib.messages",
    "django.contrib.sessions",
    "django.contrib.staticfiles",
    # third party apps

    # internal
    "crm",
]

MIDDLEWARE = [
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
]

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "django.template.context_processors.request",
            ]
        }
    }
]

DATABASES = {
    "default": {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'DatabaseName',
        'USER': 'DatabaseUserName',
        'PASSWORD': 'DatabaseUserpassword',
        'HOST': 'localhost',
        'PORT': '5432',
        'DEFAULT_AUTO_FIELD': 'django.db.models.BigAutoField',
        # "ENGINE": "django.db.backends.sqlite3",
        # "NAME": "app/data/main",
    }
}

# DEFAULT_AUTO_FIELD = {
#     "django.db.models.AutoField",
#     "django.db.models.BigAutoField",
# }