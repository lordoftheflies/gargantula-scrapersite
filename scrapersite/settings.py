"""
Django settings for scrapersite project.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""
import os

from configurations import Configuration, values


class Common(Configuration):
    # Build paths inside the project like this: os.path.join(BASE_DIR, ...)
    BASE_DIR = os.path.dirname(os.path.dirname(__file__))

    # SECURITY WARNING: keep the secret key used in production secret!
    SECRET_KEY = values.SecretValue()

    # SECURITY WARNING: don't run with debug turned on in production!
    DEBUG = values.BooleanValue(False)

    ALLOWED_HOSTS = ['*']

    # Application definition
    INSTALLED_APPS = [
        # 'material',
        # 'material.frontend',
        # # 'material.dashboard',
        # 'material.admin',

        'django.contrib.admin',
        'django.contrib.admindocs',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'corsheaders',
        # 'cubesviewer.apps.CubesviewerConfig',
        'rest_framework',

        # 'dynamic_scraper',

        # 'report_builder',
        'django_extensions',

        # 'mdm.apps.MdmConfig',
        # 'botapp.apps.BotappConfig',
        # 'reportsapp.apps.ReportsappConfig',
        # 'datastore.apps.DatastoreConfig',

        'djangobower',

        'hydra_presentation.apps.HydraPresentationConfig',

    ]

    MIDDLEWARE = [
        'django.middleware.security.SecurityMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'corsheaders.middleware.CorsMiddleware',
        'django.middleware.common.CommonMiddleware',
        'corsheaders.middleware.CorsPostCsrfMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
    ]

    ROOT_URLCONF = 'scrapersite.urls'

    TEMPLATE_LOADERS = (
        'django.template.loaders.filesystem.Loader',
        'django.template.loaders.app_directories.Loader',
        #     'django.template.loaders.eggs.Loader',
    )

    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [
                os.path.join(BASE_DIR, 'templates')
            ],
            'APP_DIRS': True,
            'OPTIONS': {
                'context_processors': [
                    'django.contrib.auth.context_processors.auth',
                    'django.template.context_processors.debug',
                    'django.template.context_processors.request',
                    'django.template.context_processors.media',
                    'django.template.context_processors.static',
                    'django.contrib.messages.context_processors.messages'
                ],
            },
        },
    ]

    # REST_FRAMEWORK = {
    #     'PAGE_SIZE': 10,
    #     'DEFAULT_AUTHENTICATION_CLASSES': (
    #         'rest_framework.authentication.SessionAuthentication',
    #     )
    # }

    CORS_ORIGIN_ALLOW_ALL = True

    REPORT_BUILDER_FRONTEND = True
    REPORT_BUILDER_ASYNC_REPORT = True
    REPORT_BUILDER_GLOBAL_EXPORT = True
    REPORT_BUILDER_EMAIL_NOTIFICATION = False
    REDIS_ADDR = os.environ.get('REDIS_1_PORT_6379_TCP_ADDR', 'localhost')
    REDIS_PORT = os.environ.get('REDIS_1_PORT_6379_TCP_PORT', '6379')

    BROKER_URL = 'redis://{}:{}/0'.format(REDIS_ADDR, REDIS_PORT)
    CELERY_RESULT_BACKEND = BROKER_URL
    # BROKER_HOST = "localhost"
    # BROKER_PORT = 5672
    # BROKER_BACKEND = "django"
    # BROKER_USER = "guest"
    # BROKER_PASSWORD = "guest"
    # BROKER_VHOST = "/"
    # CELERYBEAT_SCHEDULER = 'djcelery.schedulers.DatabaseScheduler'

    # REPORT_BUILDER_INCLUDE = ['botapp.*']  # Allow only the model user to be accessed


    WSGI_APPLICATION = 'scrapersite.wsgi.application'

    # Database
    # https://docs.djangoproject.com/en/1.11/ref/settings/#databases
    # DATABASES = values.DatabaseURLValue(
    #     'sqlite:///{}'.format(os.path.join(BASE_DIR, 'db.sqlite3'))
    # )
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': os.environ.get("DATABASE_NAME"),
            'USER': os.environ.get("DATABASE_USER"),
            'PASSWORD': os.environ.get("DATABASE_PASSWORD"),
            'HOST': os.environ.get("DATABASE_HOST"),
            'PORT': os.environ.get("DATABASE_PORT")
        }
    }

    # Password validation
    # https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators
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
    # https://docs.djangoproject.com/en/1.11/topics/i18n/
    LANGUAGE_CODE = 'en-us'

    TIME_ZONE = 'UTC'

    USE_I18N = True

    USE_L10N = True

    USE_TZ = True

    # Static files (CSS, JavaScript, Images)
    # https://docs.djangoproject.com/en/1.11/howto/static-files/
    STATIC_URL = '/static/'
    MEDIA_URL = '/media/'
    STATIC_ROOT = os.path.join(BASE_DIR, "static")
    MEDIA_ROOT = os.path.join(BASE_DIR, "media")
    STATICFILES_FINDERS = (
        'django.contrib.staticfiles.finders.FileSystemFinder',
        'django.contrib.staticfiles.finders.AppDirectoriesFinder',
        'djangobower.finders.BowerFinder',
    )

    # AUTH_USER_MODEL = 'users.User'

    LOGGING = {
        'version': 1,
        'disable_existing_loggers': True,
        'formatters': {
            'verbose': {
                'format': '%(levelname)s %(asctime)s [%(processName)s:%(threadName)s] %(module)s(%(lineno)d) %(message)s'
            },
            'simple': {
                'format': '%(levelname)s %(message)s'
            },
        },
        'handlers': {
            'file': {
                'level': 'DEBUG',
                'class': 'logging.FileHandler',
                'filename': 'console.log',
                'formatter': 'verbose'
            },
            'console': {
                'class': 'logging.StreamHandler',
                'formatter': 'verbose'
            },
        },
        'loggers': {
            'django': {
                'handlers': ['console'],
                'level': os.getenv('DJANGO_LOG_LEVEL', 'DEBUG'),
            },

            # 'botapp.views': { 'handlers': ['console'], 'level': 'DEBUG' },
            # 'botapp.forms': { 'handlers': ['console'], 'level': 'DEBUG' },
            # 'botapp.models': { 'handlers': ['console'], 'level': 'DEBUG' }
        },
        # 'cubesviewer': {
        #     'handlers': ['console'],
        #     'level': 'DEBUG',
        #     'propagate': True,
        # }
    }

    SCRAPY_DAEMON_HOST = 'http://localhost:6800/logs/portalcrawler/angular'

    ##
    # 2. Configuration of CubesViewer Server
    ##

    # Base Cubes Server URL.
    # Your Cubes Server needs to be running and listening on this URL, and it needs
    # to be accessible to clients of the application.
    CUBESVIEWER_CUBES_URL = "http://localhost:5000"

    # CubesViewer Store backend URL. It should point to this application.
    # Note that this must match the URL that you use to access the application,
    # otherwise you may hit security issues. If you access your server
    # via http://localhost:8000, use the same here. Note that 127.0.0.1 and
    # 'localhost' are different strings for this purpose. (If you wish to accept
    # requests from different URLs, you may need to add CORS support).
    CUBESVIEWER_BACKEND_URL = "http://localhost:8000/cubesviewer"

    # Optional user and password tuple to access the backend, or False
    # (only applies when CubesViewer Cubes proxy is used)
    # CUBESVIEWER_CUBES_PROXY_USER = ('user', 'password')
    CUBESVIEWER_CUBES_PROXY_USER = None

    # CubesViewer Proxy ACL
    # (only applies when CubesViewer Cubes proxy is used)
    # ie. CUBESVIEWER_PROXY_ACL = [ { "cube": "my_cube", "group": "my_group" } ]
    CUBESVIEWER_PROXY_ACL = []

    # ======================================
    # PRESENTATION LAYER
    # ======================================

    BOWER_COMPONENTS_ROOT = os.path.join(BASE_DIR, 'components')

    BOWER_INSTALLED_APPS = [
        "PolymerElements/app-layout#^2.0.0",
        "PolymerElements/app-route#^2.0.0",
        "SieBrum/brum-global-variable#^1.0.6",
        "PolymerElements/iron-ajax#^2.1.3",
        "PolymerElements/iron-flex-layout#^2.0.0",
        "PolymerElements/iron-collapse#^2.0.0",
        "PolymerElements/iron-form#^2.3.0",
        "PolymerElements/iron-iconset-svg#^2.0.0",
        "PolymerElements/iron-icon",
        "PolymerElements/iron-image#^2.2.0",
        "PolymerElements/iron-input#^2.1.1",
        "PolymerElements/iron-list#^2.0.14",
        "PolymerElements/iron-localstorage#^2.1.1",
        "PolymerElements/iron-media-query#^2.0.0",
        "PolymerElements/iron-pages#^2.0.0",
        "PolymerElements/iron-scroll-target-behavior#^2.1.1",
        "PolymerElements/iron-selector#^2.0.0",
        "PolymerElements/paper-button",
        "PolymerElements/paper-badge#^2.1.0",
        "PolymerElements/paper-card#^2.1.0",
        "PolymerElements/paper-checkbox#^2.0.2",
        "PolymerElements/paper-dialog#^2.1.1",
        "PolymerElements/paper-dropdown-menu#^2.0.3",
        "PolymerElements/paper-fab#^2.1.0",
        "PolymerElements/paper-icon-button#^2.0.0",
        "PolymerElements/paper-input#^2.2.0",
        "PolymerElements/paper-item#^2.1.1",
        "PolymerElements/paper-listbox#^2.1.1",
        "PolymerElements/paper-menu-button#^2.1.1",
        "PolymerElements/paper-progress#^2.1.0",
        "PolymerElements/paper-radio-button#^2.0.0",
        "PolymerElements/paper-radio-group#^2.1.0",
        "PolymerElements/paper-spinner#^2.1.0",
        "PolymerElements/paper-tabs#^2.0.0",
        "PolymerElements/paper-toast#^2.1.0",
        "Polymer/polymer#^2.0.0",
        "SieBrum/brum-global-variable#^1.0.6",
        "webcomponents/webcomponentsjs#^1.0.0",
        "web-animations-js#^2.3.1",
        "socket.io-client#^2.0.1",
        "chartjs#2.7.1",
        "chartjs-plugin-datalabels#0.2.0",
        "git://github.com/lordoftheflies/moment-js#^0.7.2",
        "git://github.com/lordoftheflies/plutonium-socket#master",
        "git://github.com/lordoftheflies/paper-time-picker#master",
    ]

    POLYMER_APPLICATION_ROOT = ''

    PRESENTATION = {
        'ROOT_APP': 'hydra_presentation'
    }

class Development(Common):
    """
    The in-development settings and the default configuration.
    """
    DEBUG = True

    ALLOWED_HOSTS = []

    INTERNAL_IPS = [
        '127.0.0.1'
    ]

    INSTALLED_APPS = Common.INSTALLED_APPS + [
        'debug_toolbar'
    ]

    MIDDLEWARE = Common.MIDDLEWARE + [
        'debug_toolbar.middleware.DebugToolbarMiddleware'
    ]


class Staging(Common):
    SCRAPY_DAEMON_HOST = 'https://scrapyd.cherubits.hu/logs/portalcrawler/angular'
    # Base Cubes Server URL.
    # Your Cubes Server needs to be running and listening on this URL, and it needs
    # to be accessible to clients of the application.
    CUBESVIEWER_CUBES_URL = "https://slicer.cherubits.hu"

    # CubesViewer Store backend URL. It should point to this application.
    # Note that this must match the URL that you use to access the application,
    # otherwise you may hit security issues. If you access your server
    # via http://localhost:8000, use the same here. Note that 127.0.0.1 and
    # 'localhost' are different strings for this purpose. (If you wish to accept
    # requests from different URLs, you may need to add CORS support).
    CUBESVIEWER_BACKEND_URL = "https://top.cherubits.hu/cubesviewer"

    """
    The in-staging settings.
    """
    DEBUG = True

    INSTALLED_APPS = Common.INSTALLED_APPS + [
        'debug_toolbar'
    ]

    MIDDLEWARE = Common.MIDDLEWARE + [
        'debug_toolbar.middleware.DebugToolbarMiddleware'
    ]

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': os.environ.get("DATABASE_NAME"),
            'USER': os.environ.get("DATABASE_USER"),
            'PASSWORD': os.environ.get("DATABASE_PASSWORD"),
            'HOST': os.environ.get("DATABASE_HOST"),
            'PORT': os.environ.get("DATABASE_PORT")
        }
    }


class Production(Staging):
    """
    The in-production settings.
    """

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': os.environ.get("DATABASE_NAME"),
            'USER': os.environ.get("DATABASE_USER"),
            'PASSWORD': os.environ.get("DATABASE_PASSWORD"),
            'HOST': os.environ.get("DATABASE_HOST"),
            'PORT': os.environ.get("DATABASE_PORT")
        }
    }

    # Security
    # SESSION_COOKIE_SECURE = values.BooleanValue(True)
    # SECURE_BROWSER_XSS_FILTER = values.BooleanValue(True)
    # SECURE_CONTENT_TYPE_NOSNIFF = values.BooleanValue(True)
    # SECURE_HSTS_INCLUDE_SUBDOMAINS = values.BooleanValue(True)
    # SECURE_HSTS_SECONDS = values.IntegerValue(31536000)
    # SECURE_REDIRECT_EXEMPT = values.ListValue([])
    # SECURE_SSL_HOST = values.Value(None)
    # SECURE_SSL_REDIRECT = values.BooleanValue(True)
    # SECURE_PROXY_SSL_HEADER = values.TupleValue(
    #     ('HTTP_X_FORWARDED_PROTO', 'https')
    # )
    STATIC_ROOT = '/opt/cherubits/gargantula/scrapersite/static/'
    MEDIA_ROOT = '/opt/cherubits/gargantula/scrapersite/media/'