"""
ASGI entrypoint. Configures Django and then runs the application
defined in the ASGI_APPLICATION setting.
"""

import os

import dotenv

dotenv_path = os.path.join(str(os.path.expanduser('~')), '.gargantula')
dotenv.load_dotenv(dotenv_path=dotenv_path)

ENVIRONMENT = os.getenv('ENVIRONMENT')

if ENVIRONMENT == 'STAGING':
    settings = 'staging'
elif ENVIRONMENT == 'PRODUCTION':
    settings = 'production'
else:
    settings = 'development'

from channels.routing import get_default_application
from configurations import importer


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'scrapersite.settings')
os.environ.setdefault('DJANGO_CONFIGURATION', settings.title())

importer.install()
application = get_default_application()
