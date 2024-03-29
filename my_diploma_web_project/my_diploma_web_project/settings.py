from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-5w-ci8ic5l!@w%ht^!t5glc53q)%&wyj@+s*fp_*qvr-wag7!x'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['192.168.1.136', '127.0.0.1']

# Application definition

INSTALLED_APPS = [
    'account.apps.AccountConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'main_app',
    'shop.apps.ShopConfig',
    'cart.apps.CartConfig',
    'orders.apps.OrdersConfig',
    'payment.apps.PaymentConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'my_diploma_web_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'cart.context_processors.cart',  # context processor для доступа из любого шаблона
            ],
        },
    },
]

WSGI_APPLICATION = 'my_diploma_web_project.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/


LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/


# STATIC_ROOT = BASE_DIR / 'static'

STATIC_URL = 'static/'  # python manage.py collectstatic (собрать статику)

STATICFILES_DIRS = [
    BASE_DIR / "static",
]
# media_files (files from the database)
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {  # форматы вывода логов
        "verbose": {  # вариант 1
            "format": "{levelname} - {asctime} - {module} - {process:d} - {thread:d} - {message}",
            "style": "{",
        },
        "simple": {  # вариант 2
            "format": "{levelname} {message}",
            "style": "{",
        },
    },
    "handlers": {  # варианты исхода логов
        "console": {  # в консоль
            "level": "INFO",
            "class": "logging.StreamHandler",
            "formatter": "simple",  # формат для вывода
        },
        "file": {  # в файл
            "level": "INFO",
            'class': 'logging.FileHandler',
            'filename': 'log/info.log',
            "formatter": "verbose",
        },
    },
    "loggers": {
        "django": {  # логирование проекта в целом
            "handlers": ["console", "file"],  # вывод в консоль и файл
            'level': 'INFO'
        },
        # 'my_test_app': { # каркас для будущего приложения
        #    'handlers': ['console', 'file'],
        #    'level': 'INFO',
        #    'propagate': ,

        # },
    },
}

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# LOGIN_REDIRECT_URL = 'dashboard' # переход с переменной {{ next }}
# LOGIN_URL = 'login'
# LOGOUT_URL = 'logout'


EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'  # отправка писем в консоль

# EMAIL_HOST = 'smtp.gmail.com'              # подключение службы для отправки писем
# EMAIL_HOST_USER = 'pollop888777@gmail.com'
# EMAIL_HOST_PASSWORD = '**********'
# EMAIL_PORT = 587
# EMAIL_USE_TLS = True

PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',  # хэширует пароль в бд по верхнему
    'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',  # сверяет по всем
    'django.contrib.auth.hashers.Argon2PasswordHasher',
    'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
    'django.contrib.auth.hashers.ScryptPasswordHasher',
]

CART_SESSION_ID = 'cart'  # ключ в сессии к корзине

# stripe система безналичных платежей
STRIPE_PUBLISHABLE_KEY = ('pk_test_51OIOcUCUqneCbsuDGHN9Qlzo533y0lGc0QG7xcXPPpaZH2DJILLKe24XZQ'
                          'wV3GrbYyBGcSBbQBZOfbmnsodpFDCH00hdXveNXz')  # Публикуемый ключ
STRIPE_SECRET_KEY = ('sk_test_51OIOcUCUqneCbsuDYOsXFp8lGxS6xDMQDMhE5OngR'
                     'XSX5bzJhTCwN2VNe5QBLEaU8X6DcwVfxLxEoJPTOvJJDW20004irITXTJ')  # Секретный ключ
STRIPE_API_VERSION = '2023-10-16'  # '2023-08-16'









# Для получения данных с сервера stripe
STRIPE_WEBHOOK_SECRET = 'whsec_9f9a085a0ddfd048db6c734456a703016109f76c5f6e44ef263ca9cd92db2c93'
